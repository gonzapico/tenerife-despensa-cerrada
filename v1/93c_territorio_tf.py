# -*- coding: utf-8 -*-
"""Territorio 3D de Tenerife: malla de alturas (Copernicus DEM GLO-30) y texturas 'hoy' / 'despensa cerrada'
con las parcelas del Mapa de Cultivos de Tenerife 2020-21. El reparto sobre parcelas es una ilustración del plan óptimo
(escenario insular|0.3|1|1): calor por cota (lo más cálido abajo) y, del suelo abandonado, se recupera el de menor pendiente. [INFERENCIA]
"""
import json, base64, io, numpy as np, pandas as pd, geopandas as gpd, rasterio
from rasterio import features
from rasterio.warp import reproject, Resampling
from rasterio.transform import from_bounds
from PIL import Image
DL='/tmp/claude-0/-home-user/37cffb6f-bbb3-5850-8e2c-2adc0c1ce5ef/scratchpad/tf_dl/'
BBOX=[-16.95,27.97,-16.10,28.61]; W=1440
kmx=(BBOX[2]-BBOX[0])*111.32*np.cos(np.radians(28.29)); kmy=(BBOX[3]-BBOX[1])*111.32
mpx=kmx*1000/W; H=int(round(kmy*1000/mpx)); mpy=kmy*1000/H
PASO=5; nx=int(np.ceil(W/PASO)); ny=int(np.ceil(H/PASO))
tr=from_bounds(BBOX[0],BBOX[1],BBOX[2],BBOX[3],W,H)
# ---- DEM -> rejilla de la textura
dem=np.zeros((H,W),np.float32)
with rasterio.open(DL+'tf_dem_N28_W017.tif') as r:
    reproject(rasterio.band(r,1),dem,dst_transform=tr,dst_crs='EPSG:4326',resampling=Resampling.bilinear,dst_nodata=0)
dem=np.where(dem<1,0,dem); land=dem>0
# ---- parcelas
g=gpd.read_parquet('tf_parcelas.parquet').to_crs(4326)
G={'Platanera':['Platanera','Asociación Platanera-Cítricos'],
   'Frutales':['Aguacate','Cítricos','Mango','Papaya','Templado Otras Mezclas','Templado Pepita','Templado Hueso','Subtropicales Otras Mezclas','Higuera','Olivo','Almendro','Tunera','Granado','Piña','Parchita','Pitaya','Frutos Rojos','Moringa','Asociación Cítricos-Papa','Asociación Cítricos-Hortaliza','Asociación Cítricos-Ornamentales','Asociación Templados-Papa','Asociación Templados-Millo'],
   'Viña':['Viña','Asociación Viña-Barbecho','Asociación Viña-Huerta Limpia','Asociación Viña-Papa','Asociación Viña-Templados','Asociación Viña-Hortaliza','Asociación Viña-Cítricos','Asociación Viña-Tunera'],
   'Huerta':['Huerta Limpia','Hortaliza Otras Mezclas','Huerto Familiar','Papa','Millo','Cebolla','Batata','Ñame','Leguminosa','Cereal Otros','Melón-Sandía','Fresas','Pepino'],
   'Otros':['Barbecho','Viveros','Aromáticas','Aloe','Tagasaste','Caña de Azúcar','Tabaco'],
   'Ornamentales':['Ornamentales','Strelitzias','Próteas'],'Tomate':['Tomate'],
   'SANU':['Superficie agrícola no utilizada'],'Pastoreo':['Pastoreo sobre superficie agrícola no utilizada','Pastoreo sobre superficie no agrícola']}
COL_HOY={'Platanera':'#e2cd3c','Frutales':'#cd7846','Viña':'#8c466e','Huerta':'#6eaa50','Otros':'#aaa06e','Ornamentales':'#c878aa','Tomate':'#d73c32','SANU':'#a89680','Pastoreo':'#afa58c'}
c2g={c:k for k,v in G.items() for c in v}
g['grupo']=g.crop.map(c2g); assert g.grupo.notna().all(), g[g.grupo.isna()].crop.unique()
# ---- escenario y reparto
B=json.load(open('97_balance_salida_tf.json')); ESC='insular|0.3|1|1'; R=B['rejilla'][ESC]
ret=B['c1']['platanera_ha']-B['c1']['c1_liberada_ha']
destA=[(f['nombre'],f['valor']) for f in R['filas'] if f['tipo']!='ganado' and f['bolsa']=='A']
destB=[(f['nombre'],f['valor']) for f in R['filas'] if f['tipo']!='ganado' and f['bolsa']!='A']
CALOR=['Plátano (consumo local)','Caña de azúcar (miel de caña)','Cacahuete','Papaya','Mango','Boniato','Ñame','Tomate','Millo forrajero (costa)','Millo (grano, gofio)','Calabaza y bubango','Judía seca','Cebolla','Zanahoria','Lechuga','Col','Papa',
       'Millo (medianías, regadío)','Hortalizas (medianías, regadío)','Forraje regado (medianías)','Girasol (aceite)','Olivo (aceite)','Papa (medianías, regadío)','Higo','Almendra','Garbanzo','Lenteja','Chocho','Haba seca','Arveja seca','Cebada (gofio)','Trigo (gofio)','Centeno','Papa de secano','Castaña','Pasto y tagasaste (secano)']
rank=lambda n: CALOR.index(n) if n in CALOR else 99
destA=[('Plátano (consumo local)',ret)]+sorted(destA,key=lambda d:rank(d[0])); destB=sorted(destB,key=lambda d:rank(d[0]))
def asigna(parc,dest):
    parc=parc.sort_values('z'); cum=parc.ha.cumsum().values; out=np.array(['']*len(parc),dtype=object); lo=0.0
    for n,h in dest:
        m=(cum>lo)&(cum<=lo+h); out[m]=n; lo+=h
    out[out=='']=dest[-1][0] if len(dest) else ''
    return pd.Series(out,index=parc.index)
plat=g[g.grupo=='Platanera']; g.loc[plat.index,'futuro']=asigna(plat,destA)
sanu=g[g.grupo=='SANU'].sort_values('slope'); rec=sanu[sanu.ha.cumsum()<=B['param']['SANU']*0.3]
g.loc[rec.index,'futuro']=asigna(rec,destB)
# ---- leyendas
PAL=['#eed64c','#e8a23a','#d6c35a','#b9d16a','#8ec16a','#5fa86d','#c8b04a','#a1a06e','#8aa6a0','#d78b5a','#b7d7c3','#7a9a6a']
tot=g[g.futuro.notna()].groupby('futuro').ha.sum().sort_values(ascending=False)
top=list(tot.index[:11]); COL_FUT={n:PAL[i] for i,n in enumerate(top)}
g['futuro2']=g.futuro.where(g.futuro.isin(top),'Otros destinos'); COL_FUT['Otros destinos']='#d9c9a8'
leyenda_futuro=[{'d':n,'c':COL_FUT[n],'ha':int(round(tot[n]))} for n in top]+([{'d':'Otros destinos','c':COL_FUT['Otros destinos'],'ha':int(round(tot[~tot.index.isin(top)].sum()))}] if (~tot.index.isin(top)).any() else [])
mant=g[g.futuro.isna()&g.grupo.isin(['Viña','Frutales','Huerta','Otros','Ornamentales','Tomate'])].groupby('grupo').ha.sum()
leyenda_mantiene=[{'d':k,'c':COL_HOY[k],'ha':int(round(mant[k]))} for k in ['Viña','Frutales','Huerta','Tomate','Otros','Ornamentales'] if k in mant]
leyenda_hoy=[{'d':k,'c':COL_HOY[k]} for k in COL_HOY]
# ---- zonas
def zona(lon,lat):
    if lon>-16.40 and lat>28.40: return 'Noreste (Anaga · La Laguna · Tegueste)'
    if lat>28.33 and lon>=-16.75: return 'Norte (La Orotava · Acentejo · Tacoronte)'
    if lon<-16.75 and lat>28.22: return 'Noroeste (Icod · Daute · Teno)'
    if lon<-16.62: return 'Suroeste (Guía de Isora · Adeje · Arona)'
    if lon<-16.45: return 'Sur (Granadilla · Arico · Vilaflor)'
    return 'Este (Güímar · Candelaria · Santa Cruz)'
g['zona']=[zona(a,b) for a,b in zip(g.lon,g.lat)]
zonas=[]
for zn,sub in g[g.futuro.notna()].groupby('zona'):
    t=sub.groupby('futuro').ha.sum().sort_values(ascending=False); tz=t.sum()
    zonas.append({'zona':zn,'ha':int(round(tz)),'top':[{'d':n,'ha':int(round(v)),'pct':int(round(100*v/tz))} for n,v in t.head(4).items()]})
# ---- texturas
def hex2rgb(h): return np.array([int(h[i:i+2],16) for i in (1,3,5)],np.float32)
def hillshade(z,az=315,alt=45):
    gy,gx=np.gradient(z,mpy,mpx); slope=np.arctan(np.hypot(gx,gy)); asp=np.arctan2(-gx,gy)
    a=np.radians(az); h=np.radians(alt)
    return np.clip(np.sin(h)*np.cos(slope)+np.cos(h)*np.sin(slope)*np.cos(a-asp),0,1)
hs=hillshade(dem)
stops=[(0,(74,96,62)),(500,(104,120,82)),(1100,(146,148,110)),(1900,(188,178,148)),(2800,(222,212,192)),(3715,(242,238,228))]
zz=dem.clip(0,3715); tint=np.zeros((H,W,3),np.float32)
for k in range(3): tint[...,k]=np.interp(zz,[s[0] for s in stops],[s[1][k] for s in stops])
base=tint*(0.5+0.65*hs)[...,None]
sea=hex2rgb('#224860')
def textura(col_by,field):
    img=base.copy()
    shapes=[(geom,i+1) for i,geom in enumerate(g.geometry)]
    cls=g[field].values
    ras=features.rasterize(((geom,i+1) for i,(geom,c) in enumerate(zip(g.geometry,cls)) if isinstance(c,str)),out_shape=(H,W),transform=tr,fill=0,dtype='int32')
    cols=np.zeros((len(g)+1,3),np.float32); keep=np.zeros(len(g)+1,bool)
    for i,c in enumerate(cls):
        if isinstance(c,str) and c in col_by: cols[i+1]=hex2rgb(col_by[c]); keep[i+1]=True
    m=keep[ras]
    img[m]=cols[ras][m]*(0.6+0.5*hs[m])[...,None]
    img[~land]=sea
    im=Image.fromarray(np.clip(img,0,255).astype(np.uint8)); b=io.BytesIO(); im.save(b,'JPEG',quality=82,optimize=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode(), im
g['hoy']=g.grupo
texHoy,imH=textura(COL_HOY,'hoy')
# futuro: lo que se mantiene con su color de hoy + destinos + SANU no recuperado atenuado
COLF=dict(COL_FUT); COLF.update({k:COL_HOY[k] for k in ['Viña','Frutales','Huerta','Otros','Ornamentales','Tomate','Pastoreo']}); COLF['SANU']='#968c6e'
g['fut_draw']=g.futuro2.where(g.futuro.notna(),g.grupo)
texFut,imF=textura(COLF,'fut_draw')
imH.save('tex_hoy_tf.jpg',quality=82); imF.save('tex_fut_tf.jpg',quality=82)
# ---- malla de alturas (uint16, decímetros) en los vértices
xs=np.linspace(0,W-1,nx).round().astype(int); ys=np.linspace(0,H-1,ny).round().astype(int)
z=dem[np.ix_(ys,xs)]; alt=base64.b64encode((z*10).round().astype('<u2').tobytes()).decode()
terr={'bbox':BBOX,'W':W,'H':H,'malla':[nx,ny],'paso_px':PASO,'m_por_px':[mpx,mpy],'z_max':float(dem.max()),'escenario':ESC,'leyenda_futuro':leyenda_futuro,'leyenda_mantiene':leyenda_mantiene,'leyenda_hoy':leyenda_hoy,'zonas':zonas,
      'platanera_ha':int(round(B['c1']['platanera_ha'])),'recuperada_ha':int(round(rec.ha.sum())),'parcelas':int(len(g)),
      'fuentes':['Copernicus DEM GLO-30 © DLR e.V. 2010-2014 y © Airbus Defence and Space GmbH 2014-2018, Copernicus (UE y ESA)','Mapa de Cultivos de Tenerife 2020-21 · Fuente: Gobierno de Canarias (CC BY 4.0), copia GeoParquet de fiboa/Fields of the World']}
json.dump({'terr':terr,'alt':alt,'texHoy':texHoy,'texFut':texFut},open('94_territorio_salida_tf.json','w'))
print('W,H',W,H,'malla',nx,ny,'m/px',round(mpx,1),round(mpy,1),'zmax',dem.max(),'tex KB',len(texHoy)//1024,len(texFut)//1024,'alt KB',len(alt)//1024)
print('leyenda_futuro',leyenda_futuro); print('mantiene',leyenda_mantiene); print('recuperada',rec.ha.sum()); 
for zn in zonas: print(zn)

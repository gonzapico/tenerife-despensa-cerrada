# -*- coding: utf-8 -*-
"""C1-C2 (tierra y agua que libera la platanera) y balance de suficiencia C3-C5 (pipeline multi-isla; heredado de Tenerife v4).
Programación lineal (scipy/HiGHS) con la misma estructura que el visor de La Palma: tres bolsas de tierra
(A: costa regada ex platanera; Bs: medianías secano; Br: medianías regadío), forraje, ganado, abono y pesca.
"""
import os, sys, json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import isla, out, ref, REF
C=isla()
MAPA=json.load(open(out(C,'mapa_oficial_resumen.json')))
IST_ALL=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'islas_istac_pesca.json')))
IS=IST_ALL[C['nombre']]; ISC=IST_ALL.get('Canarias',IS)
import json, numpy as np, pandas as pd
from scipy.optimize import linprog
LP=json.load(open(os.path.join(REF,'lapalma_D.json')))
ha=pd.Series(MAPA['cultivo_ha']).astype(float)
def H(*names): return float(sum(ha.get(n,0.0) for n in names))

# ---------- C1-C2 ----------
POB=IS['poblacion']['2025']   # ISTAC, cifras oficiales de población a 1-1-2025 (E30245A_000002) [VERIFICADO]
PLAT=H('Platanera')   # Mapa de Cultivos oficial de la isla [VERIFICADO]
KG_HAB=15
_rp=[r for r in IS['rendimientos'] if r['producto']=='Plátanos']
REND=round(_rp[0]['rend_kg_ha']/1000) if _rp and _rp[0]['ha_med']>=20 else 47   # t/ha, mediana ISTAC 2017-2023 de la isla si tiene platanera; si no, la de Tenerife [APROXIMADO]
ret=POB*KG_HAB/1000/REND
lib=max(PLAT-ret,0.0)   # si la isla no produce ni para su consumo, no libera nada
AG=C['agua']; DEM_AGR=AG['demanda_agraria_hm3']   # hm³/año, demanda agraria del plan hidrológico de la isla (ver config) 
SUP_REG=AG['sup_regada_ha']
dot_A=AG['dot_A'] or (round(DEM_AGR*1e6/SUP_REG,0) if DEM_AGR and SUP_REG else None)   # m³/ha·año, media del regadío de la isla
dot_B=[8760.0,11680.0]               # 15-20 L/planta·día × 1.600 plantas/ha (mismo método B que La Palma) [APROXIMADO]
dot_C=float(AG['dot_C'] or 10000)   # dotación del plátano conforme a la IPH de Canarias [APROXIMADO]
dot_D=AG.get('dot_D')   # consumo medido en la isla, si existe (Tenerife: Cabildo 2005)
MET=AG.get('metodo','C'); DOT={'A':dot_A,'B1':dot_B[0],'B2':dot_B[1],'C':dot_C,'D':dot_D}[MET]
SANU=H('Superficie agrícola no utilizada')
agua_A=lib*DOT   # agua liberada con la dotación del método por defecto de la isla
c1={'poblacion':POB,'dot_C':dot_C,'dot_D':dot_D,'metodo_defecto':MET,'rend_platanera_istac':(_rp[0]['rend_kg_ha']/1000 if _rp else None),'poblacion_fuente':'ISTAC, cifras oficiales a 1-1-2025','platanera_invernadero_ha':MAPA['platanera_invernadero_ha'],'regado_mapa_ha':MAPA['regado_ha'],'censo_2025':{'caprino':IS['ganado_2025'].get('Caprinos'),'bovino':IS['ganado_2025'].get('Bovinos'),'ovino':IS['ganado_2025'].get('Ovinos'),'porcino':IS['ganado_2025'].get('Porcinos'),'gallinas':IS['ganado_2025'].get('Gallinas')},'anio_mapa':MAPA['anio'],'isla':C['nombre'],'agua_fuente':AG['fuente'],'platanera_ha':round(PLAT,2),'c1_liberada_ha':round(lib,2),'dot_A':dot_A,'dot_B':dot_B,'demanda_agraria_hm3':DEM_AGR,'sanu_ha':round(SANU,2),'sup_regada_ha':SUP_REG,'barbecho_ha':round(H('Barbecho'),1)}
print('C1',c1,'agua liberada hm3',round(agua_A/1e6,1),'-',round(lib*dot_B[1]/1e6,1))

# ---------- Parámetros del balance (misma estructura que La Palma; coeficientes [APROXIMADO]/[CONOCIMIENTO_BASE]) ----------
P=json.loads(json.dumps(LP['param']))
P['POB']=POB; P['SUP_A']=round(lib,1); P['AGUA']=float(round(agua_A,-3)); P['SANU']=round(SANU,1)
P['MONTE_CAP']=float(C.get('monte_cap_t_ms') or round(0.35*IS['caprino_max'],-2))   # t MS/año del monte para el caprino: 0,35 t/cabra × máximo del censo caprino ISTAC 2014-2025 de la isla [APROXIMADO]
P['PESCA_T']=float(IS['pesca']['tf_t'])   # t, primera venta 2021 en puertos de la isla (registro de primera venta, Gobierno de Canarias, CC BY 4.0) [VERIFICADO]
CABRA={'tenerife':'Cabra tinerfeña','gran-canaria':'Cabra majorera (Gran Canaria)','lanzarote':'Cabra majorera','fuerteventura':'Cabra majorera','la-gomera':'Cabra majorera (La Gomera)','el-hierro':'Cabra majorera (El Hierro)'}.get(C['slug'],'Cabra')
P['GAN'][CABRA]=P['GAN'].pop('Cabra palmera'); P['LECHE'][CABRA]=P['LECHE'].pop('Cabra palmera')
CULT=json.loads(json.dumps(LP['cult']))   # rendimientos de referencia FAOSTAT España/mundo y composición (mismos que La Palma)
# ---------- v4: factor de rendimiento por cultivo medido en Tenerife (ISTAC 2017-2023) ----------
IST=pd.DataFrame(IS['rendimientos']).set_index('producto') if IS['rendimientos'] else pd.DataFrame(columns=['ha_med','t_med']).set_index(pd.Index([],name='producto'))
ISTC=pd.DataFrame(ISC['rendimientos']).set_index('producto')
REND_FUENTE={}
def rend_istac(names,minha=3.0):
    r=IST.loc[[n for n in names if n in IST.index]]
    if len(r) and r.ha_med.sum()>=minha: REND_FUENTE[tuple(names)]='isla'; return float(r.t_med.sum()*1000/r.ha_med.sum())
    r=ISTC.loc[[n for n in names if n in ISTC.index]]   # sin superficie suficiente en la isla: media de Canarias [APROXIMADO]
    if len(r) and r.ha_med.sum()>0: REND_FUENTE[tuple(names)]='canarias'; return float(r.t_med.sum()*1000/r.ha_med.sum())
    return None
MAPA_ISTAC={'Papa':['Papas tempranas','Papas extratempranas','Papas tardías','Papas media estación'],'Papa de secano':['Papas tempranas','Papas extratempranas','Papas tardías','Papas media estación'],'Papa (medianías, regadío)':['Papas tempranas','Papas extratempranas','Papas tardías','Papas media estación'],
 'Boniato':['Batatas y boniatos'],'Millo (grano, gofio)':['Maíz en grano'],'Millo (medianías, regadío)':['Maíz en grano'],'Judía seca':['Judías secas'],'Tomate':['Tomates'],'Col':['Coles','Coliflor'],'Cebolla':['Cebollas'],'Zanahoria':['Zanahorias'],
 'Calabaza y bubango':['Calabazas butternut y calabazas cucurbita máxima','Calabacines'],'Lechuga':['Lechugas'],'Plátano (consumo local)':['Plátanos'],'Papaya':['Papayas'],'Mango':['Mangos'],'Caña de azúcar (miel de caña)':['Caña de azúcar'],
 'Trigo (gofio)':['Trigo'],'Cebada (gofio)':['Cebada'],'Centeno':['Centeno'],'Garbanzo':['Leguminosas y proteaginosas secas para la producción de grano (incluidas las semillas y las mezclas de cereales y leguminosas)'],'Lenteja':['Leguminosas y proteaginosas secas para la producción de grano (incluidas las semillas y las mezclas de cereales y leguminosas)'],
 'Haba seca':['Habas'],'Arveja seca':['Guisantes'],'Chocho':['Altramuces'],'Castaña':['Castañas'],'Almendra':['Almendras'],'Higo':['Higos'],'Olivo (aceite)':['Aceitunas para aceite'],'Hortalizas (medianías, regadío)':['Hortalizas frescas (incluidos los melones)']}
F_DEF=P['F_CON']   # 0,7 para los cultivos sin dato tinerfeño (cacahuete, girasol, ñame) [APROXIMADO]
for c,k in CULT.items():
    r=rend_istac(MAPA_ISTAC.get(c,[]))
    if r:
        k['rend_tf']=round(r); k['f_tf']=round(r/k['rend'],3); k['fuente_rend']='ISTAC 2017-2023, '+('isla' if REND_FUENTE.get(tuple(MAPA_ISTAC.get(c,[])))=='isla' else 'media de Canarias [APROXIMADO]')
        if c=='Papa de secano': k['f_tf']=round(r/CULT['Papa']['rend'],3)   # el secano hereda la relación de la papa
    else: k['rend_tf']=None; k['f_tf']=F_DEF; k['fuente_rend']='FAOSTAT × 0,7 [APROXIMADO]'
# ---------- v5 (multi-isla): viabilidad climática de cada cultivo del balance según el catálogo ECOCROP de la isla [DECISIÓN v5] ----------
# Bs (secano) solo si el catálogo da VIABLE SECANO, o VIABLE CON RIEGO con déficit ≤150 mm respecto al óptimo (secano tradicional con lluvia algo escasa);
# A y Br solo si es VIABLE SECANO o VIABLE CON RIEGO. Las excluidas quedan a 0 en el modelo. En Tenerife v4 no excluye ninguna (reproduce v4).
CAT={c['n']:c for c in json.load(open(out(C,'95_catalogo_salida.json')))['cat']}
CLIMA=json.load(open(out(C,'92c_pisos_salida.json')))['clima']
MAPA_CAT={'Papa':'Papa','Papa de secano':'Papa','Papa (medianías, regadío)':'Papa','Boniato':'Boniato','Millo (grano, gofio)':'Millo (grano)','Millo (medianías, regadío)':'Millo (grano)','Judía seca':'Judía seca / habichuela','Ñame':'Ñame (Colocasia, local)','Tomate':'Tomate','Col':'Col / repollo','Cebolla':'Cebolla seca','Zanahoria':'Zanahoria y nabo','Calabaza y bubango':'Calabaza / bubango','Lechuga':'Lechuga y escarola','Plátano (consumo local)':'Plátano','Papaya':'Papaya','Mango':'Mango','Caña de azúcar (miel de caña)':'Caña de azúcar','Cacahuete':'Cacahuete','Trigo (gofio)':'Trigo','Cebada (gofio)':'Cebada','Centeno':'Centeno','Garbanzo':'Garbanzo','Lenteja':'Lenteja','Haba seca':'Haba seca','Arveja seca':'Arveja seca','Chocho':'Chocho / altramuz','Castaña':'Castaña','Almendra':'Almendra','Higo':'Higo','Olivo (aceite)':'Aceituna / olivo','Girasol (aceite)':'Girasol'}
DEF_SECANO=150
EXCLUIDOS={}
for c,k in CULT.items():
    e=CAT.get(MAPA_CAT.get(c,''))
    if e is None: k['viab']='sin entrada en el catálogo (se admite)'; k['excluido']=False; continue
    k['viab']=e['c']+(f" (déficit {e['r']} mm)" if e['c']=='VIABLE CON RIEGO' else '')
    if k['bolsa']=='Bs': ok=(e['c']=='VIABLE SECANO') or (e['c']=='VIABLE CON RIEGO' and e['r']<=DEF_SECANO)
    else: ok=e['c'] in ('VIABLE SECANO','VIABLE CON RIEGO')
    k['excluido']=not ok
    if not ok: EXCLUIDOS[c]=k['viab']
if EXCLUIDOS: print('Cultivos excluidos del balance por el catálogo de la isla:',EXCLUIDOS)
# forraje de secano: 3 t MS/ha con ≥500 mm en el piso más lluvioso; por debajo se reduce proporcionalmente a la lluvia (islas secas) [APROXIMADO] [DECISIÓN v5]
_llmax=max([c['lluvia_mm'] for c in CLIMA if c['lluvia_mm'] is not None] or [500])
for _n,_f in P['FORRAJE'].items():
    if _f[0]=='Bs' and _llmax<500: _f[1]=round(_f[1]*_llmax/500,2); print('forraje secano',_n,'→',_f[1],'t MS/ha (lluvia máx.',_llmax,'mm)')
def fesc(esc,c):   # factor de rendimiento por escenario y cultivo
    f=CULT[c]['f_tf']
    return {'insular':f,'espana':max(f,1.0),'autarquia':f}[esc]
F={'autarquia':None,'insular':None,'espana':None}

# ---------- Producción actual sin plátano (bases) ----------
# constantes por cultivo derivadas de las bases de La Palma (kcal/prot/grasa por t producida y kg comestibles por t), rendimiento FAOSTAT × factor
def derive(name,istac=None):
    r=[b for b in LP['bases']['insular'] if b['cultivo']==name][0]
    t=r['t']; rf=r['t']/r['ha']/0.7*1000; rt=rend_istac(istac or [])   # kg/ha (en v1-v3 quedó en t/ha y la producción actual de estos cultivos salía mil veces menor)
    return dict(rend=rf, rend_tf=rt, kf=r['kcal']/(t*1e4), pf=r['prot']/(t*1e4), gf=r['grasa']/(t*1e4), fyh=r['fyh']/t)
def from_cult(name,fyh=None):
    c=CULT[name]; return dict(rend=c['rend'], rend_tf=c.get('rend_tf'), kf=c['kcal']*c['frac'], pf=c['prot']*c['frac'], gf=c['grasa']*c['frac'], fyh=(1000*c['frac'] if (c['fyh'] if fyh is None else fyh) else 0))
K={'Aguacate':derive('Aguacate',['Aguacates']),'Viña (uva)':derive('Viña (uva)',['Uvas de vinificación','Uvas de mesa']),'Cítricos':derive('Cítricos',['Cítricos']),'Papa':derive('Papa',MAPA_ISTAC['Papa']),'Almendro':derive('Almendro',['Almendras']),'Mango':derive('Mango',['Mangos']),
   'Hortalizas':derive('Hortalizas',['Hortalizas frescas (incluidos los melones)']),'Olivo (aceite)':derive('Olivo (aceite)',['Aceitunas para aceite']),'Higuera':derive('Higuera',['Higos']),'Boniato':derive('Boniato',['Batatas y boniatos']),'Ñame':derive('Ñame'),'Millo':derive('Millo',['Maíz en grano']),'Plátano retenido':derive('Plátano retenido',['Plátanos']),
   'Cereal (trigo y cebada, gofio)':from_cult('Trigo (gofio)'),'Papaya':from_cult('Papaya'),'Leguminosa seca':from_cult('Judía seca'),
   'Frutales templados':dict(rend=15000,rend_tf=rend_istac(['Manzanas','Peras','Melocotones','Ciruelas']),kf=52*0.9,pf=0.3*0.9,gf=0.2*0.9,fyh=900),
   'Subtropicales (guayaba, chirimoya…)':dict(rend=8000,rend_tf=rend_istac(['Guayabos','Chirimoyas','Piñas tropicales','Granadas']),kf=70*0.7,pf=1.2*0.7,gf=0.5*0.7,fyh=700),
   'Tunera':dict(rend=8000,rend_tf=rend_istac(['Chumberas']),kf=41*0.6,pf=0.7*0.6,gf=0.5*0.6,fyh=600)}
for n,k in K.items():
    if k.get('rend_tf') is None: k['rend_tf']=0.7*k['rend']   # sin dato ISTAC: FAOSTAT × 0,7 [APROXIMADO]
HA_BASE={'Viña (uva)':H('Viña','Asociación Viña-Barbecho','Asociación Viña-Huerta Limpia','Asociación Viña-Papa','Asociación Viña-Templados','Asociación Viña-Hortaliza','Asociación Viña-Cítricos','Asociación Viña-Tunera'),
 'Hortalizas':H('Huerta Limpia','Hortaliza Otras Mezclas','Huerto Familiar','Tomate','Cebolla','Melón-Sandía','Pepino','Fresas','Asociación Cítricos-Hortaliza'),
 'Papa':H('Papa','Asociación Templados-Papa','Asociación Cítricos-Papa'),'Aguacate':H('Aguacate'),'Cereal (trigo y cebada, gofio)':H('Cereal Otros'),
 'Frutales templados':H('Templado Otras Mezclas','Templado Pepita','Templado Hueso'),'Subtropicales (guayaba, chirimoya…)':H('Subtropicales Otras Mezclas','Piña','Parchita','Pitaya','Granado'),
 'Cítricos':H('Cítricos'),'Millo':H('Millo','Asociación Templados-Millo'),'Papaya':H('Papaya'),'Olivo (aceite)':H('Olivo'),'Mango':H('Mango'),'Leguminosa seca':H('Leguminosa'),
 'Higuera':H('Higuera'),'Tunera':H('Tunera'),'Boniato':H('Batata'),'Almendro':H('Almendro'),'Ñame':H('Ñame'),'Plátano retenido':min(ret,PLAT)}
HA_BASE={k:v for k,v in HA_BASE.items() if v>0}
bases={}
for esc in ['autarquia','insular','espana']:
    rows=[]
    for n,h in HA_BASE.items():
        k=K[n]; rt=k['rend_tf']; f={'autarquia':5/7,'insular':1.0,'espana':max(1.0,k['rend']/rt)}[esc]; t=h*rt*f/1000
        rows.append({'cultivo':n,'ha':round(float(h),1),'t':int(round(t)),'kcal':t*1e4*k['kf'],'prot':t*1e4*k['pf'],'grasa':t*1e4*k['gf'],'fyh':t*k['fyh']})
    bases[esc]=rows
MANTIENE_HA=sum(float(v) for n,v in HA_BASE.items() if n!='Plátano retenido')

# ---------- Modelo LP ----------
need=[POB*P['NEC']['kcal']*365, POB*P['NEC']['prot']*365, POB*P['NEC']['grasa']*365]
need_fyh=POB*P['FYH_DIA']/1000*365   # kg comestibles
cults=list(CULT.keys()); forr=list(P['FORRAJE'].keys()); gans=list(P['GAN'].keys())
def aporte_cult(c,f): # por ha: kcal, prot, grasa, fyh(kg), agua
    k=CULT[c]; g=k['rend']*f*k['frac']*1000
    return np.array([g*k['kcal']/100, g*k['prot']/100, g*k['grasa']/100]), (k['rend']*f*k['frac'] if k['fyh'] else 0.0), k['agua']
def aporte_gan(g):
    ms,leche,carne,n=P['GAN'][g]; a=np.zeros(3)
    if leche: l=P['LECHE'][g]; a+=np.array([leche*10*l[0],leche*10*l[1],leche*10*l[2]])
    a+=np.array([carne*10*P['CARNE'][0],carne*10*P['CARNE'][1],carne*10*P['CARNE'][2]]); return a
def resolver(esc,frac,pm,gan):
    supB=P['SANU']*frac; capA=P['SUP_A']
    pesca_t=P['PESCA_T']*pm; kgP=pesca_t*1000*P['PESCA'][0]
    pes=np.array([kgP*10*P['PESCA'][1],kgP*10*P['PESCA'][2],kgP*10*P['PESCA'][3]])
    base=np.array([sum(b[k] for b in bases[esc]) for k in ['kcal','prot','grasa']]); base_fyh=sum(b['fyh'] for b in bases[esc])
    # variables: cultivos (sin/con abono en autarquía), forrajes, ganado, z
    var=[]  # (tipo,nombre,f,abonado)
    for c in cults:
        if esc=='autarquia':
            if CULT[c]['leg']: var.append(('cultivo',c,fesc('autarquia',c),False))
            else: var.append(('cultivo',c,round(fesc('autarquia',c)*P['F_SIN']/P['F_CON'],4),False)); var.append(('cultivo',c,fesc('autarquia',c),True))
        else: var.append(('cultivo',c,fesc(esc,c),False))
    for fo in forr: var.append(('forraje',fo,None,False))
    for g in gans: var.append(('ganado',g,None,False))
    nv=len(var)+1; iz=nv-1
    A_ub=[]; b_ub=[]
    def row(): return np.zeros(nv)
    # tierra A y B
    rA=row(); rB=row(); rW=row(); rF=row(); rN=row(); rFyh=row(); rM=row()
    nut=[row(),row(),row()]
    for i,(t,n,f,ab) in enumerate(var):
        if t=='cultivo':
            b=CULT[n]['bolsa']; (rA if b=='A' else rB)[i]=1
            a,fyh,agua=aporte_cult(n,f); rW[i]=agua; rFyh[i]=-fyh
            for k in range(3): nut[k][i]=-a[k]
            if ab: rN[i]=P['N_REQ']
        elif t=='forraje':
            b,tms,agua=P['FORRAJE'][n]; (rA if b=='A' else rB)[i]=1; rW[i]=agua; rF[i]=-tms
        else:
            ms,leche,carne,nn=P['GAN'][n]; rF[i]=ms*(1-P['MONTE_MS']) if 'Cabra' in n else ms; rM[i]=ms*P['MONTE_MS'] if 'Cabra' in n else 0; rN[i]=-nn*P['N_DISP']
            a=aporte_gan(n)
            for k in range(3): nut[k][i]=-a[k]
    A_ub+= [rA,rB,rW]; b_ub+=[capA,supB,P['AGUA']]
    if gan: A_ub.append(rF); b_ub.append(0); A_ub.append(rM); b_ub.append(P['MONTE_CAP'])
    if esc=='autarquia': A_ub.append(rN); b_ub.append(0)
    for k in range(3):
        r=nut[k]/need[k]; r[iz]=1.0; A_ub.append(r); b_ub.append((base[k]+pes[k])/need[k])
    # cuota por cultivo (suma de sus variables) ≤ CUOTA × bolsa
    for c in cults:
        r=row()
        for i,(t,n,f,ab) in enumerate(var):
            if t=='cultivo' and n==c: r[i]=1
        A_ub.append(r); b_ub.append(P['CUOTA']*(capA if CULT[c]['bolsa']=='A' else supB))
    bounds=[(0,None)]*nv
    for i,(t,n,f,ab) in enumerate(var):
        if t=='cultivo' and CULT[n].get('excluido'): bounds[i]=(0,0)   # no viable en la isla según el catálogo [DECISIÓN v5]
    if not gan:
        for i,(t,n,f,ab) in enumerate(var):
            if t!='cultivo': bounds[i]=(0,0)
    cobj=np.zeros(nv); cobj[iz]=-1
    # frutas y hortalizas: cuarta cobertura dentro de z (misma proporción que energía, proteína y grasa) [DECISIÓN v1]
    rF2=rFyh/need_fyh; rF2[iz]=1.0
    res=linprog(cobj,A_ub=np.array(A_ub+[rF2]),b_ub=np.array(b_ub+[base_fyh/need_fyh]),bounds=bounds,method='highs')
    if res.status!=0:
        print('LP no factible',esc,frac,pm,gan,res.message)
        res=linprog(cobj,A_ub=np.array(A_ub),b_ub=np.array(b_ub),bounds=bounds,method='highs')
    x=res.x; z=x[iz]
    tot=base+pes; fyh=base_fyh; agua=0.0; filas=[]; tA=0; tB=0
    for i,(t,n,f,ab) in enumerate(var):
        v=x[i]
        if v<0.5: continue
        if t=='cultivo':
            a,fy,ag=aporte_cult(n,f); tot+=v*a; fyh+=v*fy; agua+=v*ag
            if CULT[n]['bolsa']=='A': tA+=v
            else: tB+=v
            filas.append({'tipo':'cultivo','nombre':n,'valor':round(v,1),'bolsa':CULT[n]['bolsa'],'t':int(round(v*CULT[n]['rend']*f/1000)),'agua':int(round(v*ag)),'abonado':ab,'f':f,'kcal':round(v*a[0],1),'prot':round(v*a[1],2),'grasa':round(v*a[2],2)})
        elif t=='forraje':
            b,tms,ag=P['FORRAJE'][n]; agua+=v*ag; (tA if False else None)
            if b=='A': tA+=v
            else: tB+=v
            filas.append({'tipo':'forraje','nombre':n,'valor':round(v,1),'bolsa':b,'t_ms':int(round(v*tms)),'agua':int(round(v*ag)),'kcal':0.0,'prot':0.0,'grasa':0.0})
        else:
            ms,leche,carne,nn=P['GAN'][n]; a=aporte_gan(n); tot+=v*a
            filas.append({'tipo':'ganado','nombre':n,'valor':round(v,1),'leche_t':int(round(v*leche/1000)),'carne_t':int(round(v*carne/1000)),'n_t':round(v*nn*P['N_DISP']/1000,1),'kcal':round(v*a[0],1),'prot':round(v*a[1],2),'grasa':round(v*a[2],2)})
    cob={k:round(tot[i]/need[i],4) for i,k in enumerate(['kcal','prot','grasa'])}
    return {'ok':res.status==0,'z':round(z,4),'cob':cob,'cob_fyh':round(fyh/need_fyh,4),'cob_base':{k:round(base[i]/need[i],4) for i,k in enumerate(['kcal','prot','grasa'])},
            'cob_pesca':{k:round(pes[i]/need[i],4) for i,k in enumerate(['kcal','prot','grasa'])},'agua_usada':round(agua,1),'filas':filas,'pesca_t':pesca_t,'tierraA':round(tA,1),'tierraB':round(tB,2),'supB':round(supB,2)}
rej={}
for esc in ['autarquia','insular','espana']:
    for fs in range(11):
        for pm in (1,3):
            for gan in (0,1):
                rej[f'{esc}|{fs/10:.1f}|{pm}|{gan}']=resolver(esc,fs/10,pm,gan)
k='insular|0.3|1|1'; r=rej[k]
print(k,'z',r['z'],r['cob'],'fyh',r['cob_fyh'],'base',r['cob_base'],'pesca',r['cob_pesca'],'agua',r['agua_usada']/1e6)
for f in r['filas']: print('   ',f['tipo'],f['nombre'],f['valor'],f.get('bolsa',''),f.get('t',f.get('t_ms',f.get('leche_t'))))
for kk in ['autarquia|0.0|1|0','autarquia|0.3|1|1','autarquia|1.0|1|1','insular|1.0|3|1','espana|1.0|3|1','insular|0.0|1|0']:
    print(kk, rej[kk]['z'], rej[kk]['cob'], 'fyh',rej[kk]['cob_fyh'])
json.dump({'c1':c1,'param':P,'cult':CULT,'excluidos':EXCLUIDOS,'bases':bases,'rejilla':rej,'mantiene_ha':round(MANTIENE_HA,1),'rend_bases':{n:{'rend_fao':round(k['rend']),'rend_tf':round(k['rend_tf'])} for n,k in K.items()}},open(out(C,'97_balance_salida.json'),'w'),ensure_ascii=False)

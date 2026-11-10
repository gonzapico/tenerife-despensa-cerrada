# -*- coding: utf-8 -*-
"""Parcelas del Mapa de Cultivos de la isla con cota y pendiente del DEM Copernicus; resumen oficial."""
import sys, json, glob, numpy as np, pandas as pd, geopandas as gpd, rasterio
from rasterio.merge import merge
from common import isla, out, ref
c=isla()
shp=glob.glob(ref(f"shp/**/{c['shp']}"),recursive=True)
if not shp: raise SystemExit('falta el shapefile en _ref/shp/: '+c['shp'])
g=gpd.read_file(shp[0]).rename(columns={'CULTIVO_NA':'crop','CULTIVO_CO':'code'})
g=g[g.crop.notna()].copy(); g['ha']=g.geometry.area/1e4
cen=gpd.GeoSeries(g.geometry.centroid,crs=g.crs).to_crs(4326); xs=cen.x.values; ys=cen.y.values
srcs=[rasterio.open(ref(f"dem/{t}.tif")) for t in c['dem']]
dem,tr=merge(srcs); dem=dem[0]; [s.close() for s in srcs]
rows,cols=rasterio.transform.rowcol(tr,xs,ys); rows=np.clip(np.array(rows),1,dem.shape[0]-2); cols=np.clip(np.array(cols),1,dem.shape[1]-2)
z=dem[rows,cols]; mx=111320*np.cos(np.radians(np.mean(ys)))*tr.a; my=111320*abs(tr.e)
dzdx=(dem[rows,cols+1]-dem[rows,cols-1])/(2*mx); dzdy=(dem[rows-1,cols]-dem[rows+1,cols])/(2*my)
g['z']=np.maximum(z,0); g['slope']=np.degrees(np.arctan(np.hypot(dzdx,dzdy))); g['lon']=xs; g['lat']=ys
keep=['ISLA_NA','CATEGORIA','AGRUPACION','crop','code','REGADIO_NA','REGADIO_CO','TECNICA_NA','ABANDON_NA','DISEMI_NA','BORDE_NA','AREA_M2','FECHA','ha','z','slope','lon','lat','geometry']
g=g[[k for k in keep if k in g.columns]]
g.to_parquet(out(c,'parcelas.parquet'))
byc=g.groupby('crop').agg(ha=('ha','sum'),reg=('ha',lambda s: s[g.loc[s.index,'REGADIO_CO']==1].sum())); byc['pct_reg']=(100*byc.reg/byc.ha).round(0)
fechas=pd.to_datetime(g.FECHA,dayfirst=True,errors='coerce')
res={'isla':c['nombre'],'fichero':c['shp'],'parcelas':int(len(g)),'ha_total':round(float(g.ha.sum()),1),'regado_ha':round(float(g[g.REGADIO_CO==1].ha.sum()),1),
     'fecha':[str(fechas.min().date()),str(fechas.max().date())],'anio':int(fechas.max().year),
     'regado_100':byc[(byc.pct_reg>=95)&(byc.ha>=5)].index.tolist(),'sanu_abandon':g[g.crop=='Superficie agrícola no utilizada'].groupby('ABANDON_NA').ha.sum().round(1).to_dict(),
     'categoria_ha':g.groupby('CATEGORIA').ha.sum().round(1).to_dict(),'cultivo_ha':byc.ha.round(1).to_dict(),
     'invernadero_ha':round(float(g[g.TECNICA_NA=='Invernadero'].ha.sum()),1),'platanera_ha':round(float(g[g.crop=='Platanera'].ha.sum()),2),
     'platanera_invernadero_ha':round(float(g[(g.crop=='Platanera')&(g.TECNICA_NA=='Invernadero')].ha.sum()),1),'sanu_ha':round(float(g[g.crop=='Superficie agrícola no utilizada'].ha.sum()),2),
     'barbecho_ha':round(float(g[g.crop=='Barbecho'].ha.sum()),1),'bbox':[round(float(v),4) for v in g.to_crs(4326).total_bounds],'z_max_parcelas':round(float(g.z.max()))}
json.dump(res,open(out(c,'mapa_oficial_resumen.json'),'w'),ensure_ascii=False,indent=0)
print(c['nombre'],res['parcelas'],'parcelas',res['ha_total'],'ha | platanera',res['platanera_ha'],'| SANU',res['sanu_ha'],'| regado',res['regado_ha'],'| año',res['anio'],'| z max',res['z_max_parcelas'])

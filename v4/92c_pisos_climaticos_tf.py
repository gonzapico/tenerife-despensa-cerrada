# -*- coding: utf-8 -*-
"""Pisos climáticos de Tenerife v3: diez pisos (cinco cotas × vertientes N y S) a partir de estaciones reales.
Fuentes (datos_clima/):
  - aemet_normales_tenerife_1991-2020.csv  · AEMET OpenData, normales 1991-2020 (estaciones principales) [VERIFICADO]
  - aemet_medias_estaciones_2009-2025.csv   · AEMET OpenData, medias de las series mensuales 2009-2025 (estaciones automáticas, periodo corto) [APROXIMADO]
  - agrocabildo_temperatura_estaciones_2001-2007.csv · Cabildo de Tenerife, Agrocabildo, «Temperatura del aire, análisis 2008» [APROXIMADO]
  - agrocabildo_transectos_lluvia_1983-2010.csv · Cabildo de Tenerife, Agrocabildo, Santana Pérez (2012) «¿Existe cambio pluviométrico…?», 224 pluviómetros [VERIFICADO]
Método: temperatura = regresión lineal sobre la cota por vertiente con las estaciones por debajo de 1.300 m (bajo la inversión térmica) y, para la cumbre, interpolación hacia Izaña (medias cortas corregidas al periodo 1991-2020 con el sesgo
de las estaciones principales); lluvia = mediana de las estaciones de cada franja de cota y vertiente (AEMET + Agrocabildo, media de las décadas disponibles);
mínima absoluta = regresión de la media de la mínima absoluta del mes frío (AEMET). Horas de frío: relación empírica heredada de La Palma.
"""
import os
REF=os.environ.get('DESPENSA_REF',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','_ref'))
import csv, json, numpy as np
D=json.load(open(os.path.join(REF,'lapalma_D.json')))
COTAS=[(0,300),(300,600),(600,1000),(1000,1500),(1500,3715)]; NOMBRES=['Costa','Medianías bajas','Medianías altas','Pinar y cumbre baja','Cumbre']; ZREF=[150,450,800,1250,1900]
def rd(f): return list(csv.DictReader(open(f,encoding='utf-8')))
def fl(x):
    try: return float(x)
    except: return None
def band(a): return next(i for i,(lo,hi) in enumerate(COTAS) if lo<=a<hi)
# ---- vertiente por posición: N = barlovento (norte y noreste), S = sotavento (sur, este, oeste)
def vert_latlon(lat,lon):   # lat/lon AEMET en ddmmssN
    la=int(lat[:2])+int(lat[2:4])/60+int(lat[4:6])/3600; lo=-(int(lon[:2])+int(lon[2:4])/60+int(lon[4:6])/3600)
    # eje de la dorsal NE-SO: barlovento al norte de la línea que une Teno (28.35,-16.92) y Anaga (28.55,-16.15), pasando por el Teide
    return 'N' if la > 28.27 + (lo+16.92)*(28.55-28.27)/(-16.15+16.92) - 0.02 else 'S'
NORTE_AGRO=['ACENTEJO','OROTAVA','ICODEN','DAUTE','ANAGA - TRANSECTO NORESTE','ANAGA - TRANSECTO NOROESTE']
COMARCA_N=['COMARCA DE ACENTEJO','VALLE DE LA OROTAVA','COMARCA DE ICODEN','COMARCA DE DAUTE']
# ---- estaciones de temperatura
T=[]
norm=rd('datos_clima/aemet_normales_tenerife_1991-2020.csv'); med=rd('datos_clima/aemet_medias_estaciones_2009-2025.csv'); agro=rd('datos_clima/agrocabildo_temperatura_estaciones_2001-2007.csv')
nm={r['idema']:r for r in norm}
# sesgo periodo corto vs normales (estaciones con ambas)
bias=[fl(m['tm_anual'])-fl(nm[m['idema']]['tm_anual']) for m in med if m['idema'] in nm and fl(nm[m['idema']]['tm_anual']) and fl(m['tm_anual'])]
BIAS=round(float(np.mean(bias)),2)
for r in norm:
    if fl(r['tm_anual']) is None: continue
    T.append(dict(src='AEMET normales 1991-2020',nombre=r['nombre'],alt=int(r['alt']),vert=vert_latlon(r['lat'],r['lon']),tm=fl(r['tm_anual']),tf=fl(r['tm_mes_frio']),tn=fl(r['tn_mes_frio']),tc=fl(r['tm_mes_calido']),tamin=fl(r['ta_min_media']),peso=3))
for r in med:
    if r['idema'] in nm and fl(nm[r['idema']]['tm_anual']) is not None: continue
    if fl(r['tm_anual']) is None or int(r['anos_T'])<4: continue
    T.append(dict(src='AEMET medias 2009-2025 (−sesgo)',nombre=r['nombre'],alt=int(r['alt']),vert=vert_latlon(r['lat'],r['lon']),tm=fl(r['tm_anual'])-BIAS,tf=fl(r['tm_mes_frio'])-BIAS,tn=fl(r['tn_mes_frio'])-BIAS,tc=fl(r['tm_mes_calido'])-BIAS,tamin=(fl(r['ta_min_media'])-BIAS if fl(r['ta_min_media']) is not None else None),peso=2))
for r in agro:
    if fl(r['tmedia']) is None or fl(r['inv']) is None or fl(r['ver']) is None: continue
    v='N' if r['comarca'] in COMARCA_N else 'S'
    if r['comarca']=='COMARCA DE ANAGA': v='S'
    T.append(dict(src='Agrocabildo 2001-2007',nombre=r['estacion'],alt=int(r['alt']),vert=v,tm=fl(r['tmedia']),tf=fl(r['inv']),tn=None,tc=fl(r['ver']),tamin=None,peso=1))
def fit(pts,key):
    xs=np.array([p['alt'] for p in pts if p.get(key) is not None]); ys=np.array([p[key] for p in pts if p.get(key) is not None]); ws=np.array([p['peso'] for p in pts if p.get(key) is not None])
    a,b=np.polyfit(xs,ys,1,w=np.sqrt(ws)); return a,b,len(xs)
# ---- lluvia
P=[]
tr=rd('datos_clima/agrocabildo_transectos_lluvia_1983-2010.csv')
for r in tr:
    vals=[fl(r[k]) for k in ('p1983','p1990','p2000') if fl(r[k]) is not None]
    if not vals: continue
    v='N' if any(k in r['comarca'] for k in NORTE_AGRO) else 'S'
    P.append(dict(src='Agrocabildo 1983-2010',nombre=r['estacion'],alt=int(r['alt']),vert=v,p=float(np.mean(vals))))
for r in norm:
    if fl(r['p_anual']) is not None: P.append(dict(src='AEMET normales 1991-2020',nombre=r['nombre'],alt=int(r['alt']),vert=vert_latlon(r['lat'],r['lon']),p=fl(r['p_anual'])))
for r in med:
    if (r['idema'] in nm and fl(nm[r['idema']]['p_anual']) is not None) or fl(r['p_anual']) is None or int(r['anos_P'])<5: continue
    P.append(dict(src='AEMET medias 2009-2025',nombre=r['nombre'],alt=int(r['alt']),vert=vert_latlon(r['lat'],r['lon']),p=fl(r['p_anual'])))
_hf=sorted([(c['tm_mes_frio'],c['horas_frio']) for c in D['clima']])
def horas_frio(t): return float(np.interp(t,[a for a,_ in _hf],[b for _,b in _hf]))
clima=[]; ajuste={}; lluvia_tab={}
for v in ['N','S']:
    pts=[p for p in T if p['vert']==v and p['alt']<=1300]   # por debajo de la inversión térmica; la cumbre se interpola hacia Izaña
    co={k:fit(pts,k) for k in ['tm','tf','tn','tc','tamin']}
    IZ={'tm':10.5,'tf':4.7,'tn':1.4,'tc':18.5,'tamin':-4.1}   # Izaña, normales 1991-2020 (2.369 m), común a las dos vertientes
    ajuste[v]={k:{'pendiente_por_100m':round(float(100*co[k][0]),2),'ordenada':round(float(co[k][1]),2),'n':int(co[k][2])} for k in co}
    for i,z in enumerate(ZREF):
        def est(k):
            if z<=1300: return round(float(co[k][0]*z+co[k][1]),1)
            y4=co[k][0]*1250+co[k][1]; return round(float(y4+(IZ[k]-y4)*(z-1250)/(2369-1250)),1)
        band_p=[p['p'] for p in P if p['vert']==v and band(p['alt'])==i]
        ll=int(round(float(np.median(band_p)))) if band_p else None
        lluvia_tab[f'P{i+1}-{v}']={'n':len(band_p),'mediana':ll,'p25':int(np.percentile(band_p,25)) if band_p else None,'p75':int(np.percentile(band_p,75)) if band_p else None}
        tf=est('tf')
        clima.append({'piso':f'P{i+1}-{v}','nombre':NOMBRES[i],'cota':f'{COTAS[i][0]}-{COTAS[i][1]}','z_ref':z,'tm_anual':est('tm'),'tm_mes_frio':tf,'tn_mes_frio':est('tn'),'t_abs_min_est':est('tamin'),'tm_mes_calido':est('tc'),'lluvia_mm':ll,'horas_frio':int(round(horas_frio(tf))),'n_pluviometros':len(band_p)})
out={'clima':clima,'ajuste_temperatura':ajuste,'sesgo_2009_2025_vs_normales':BIAS,'lluvia_por_piso':lluvia_tab,'estaciones_temperatura':T,'estaciones_lluvia':P,
     'fuentes':['AEMET OpenData, valores climatológicos normales 1991-2020 y series mensuales 2009-2025 (16 estaciones de Tenerife)','Cabildo de Tenerife, Agrocabildo: Temperatura del aire, análisis 2008 (40 estaciones, medias 2001-2007)','Cabildo de Tenerife, Agrocabildo, L. M. Santana Pérez (2012): ¿Existe cambio pluviométrico en los últimos 40 años en Tenerife? Transectos pluviométricos 1983-2010 (224 pluviómetros)'],
     'nota':'Temperaturas por regresión sobre la cota con todas las estaciones de cada vertiente; lluvia por mediana de los pluviómetros de cada franja; la vertiente norte (barlovento) incluye el noreste y la sur (sotavento) el este y el oeste.'}
json.dump(out,open('92c_pisos_salida_tf.json','w'),ensure_ascii=False,indent=0)
print('sesgo 2009-2025 vs normales:',BIAS,'°C'); 
for v in 'NS': print(v,ajuste[v])
for c in clima: print(c)

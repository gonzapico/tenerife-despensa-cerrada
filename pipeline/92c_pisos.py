# -*- coding: utf-8 -*-
"""Pisos climáticos de una isla (pipeline multi-isla): cotas × vertientes (N barlovento, S sotavento) a partir de estaciones reales.
Fuentes: AEMET OpenData (normales 1991-2020 y medias de las series mensuales 2009-2025, corregidas del sesgo medido donde hay ambas) y,
en Tenerife, la red de Agrocabildo (temperaturas 2001-2007 y 224 pluviómetros 1983-2010).
Método: temperatura por regresión lineal sobre la cota por vertiente con las estaciones por debajo de la inversión (si una vertiente tiene
menos de 3 estaciones se usan todas las de la isla); lluvia por mediana de los pluviómetros de cada franja y vertiente, y donde una franja
no tiene pluviómetro, regresión del logaritmo de la lluvia sobre la cota con las estaciones de la isla. Horas de frío: relación empírica heredada de La Palma."""
import os, sys, json, csv, statistics as st, numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import isla, out, ref, lado_norte, dms
C=isla(); D=json.load(open(ref('lapalma_D.json')))
MAPA=json.load(open(out(C,'mapa_oficial_resumen.json'))); bb=MAPA['bbox']
def inbox(lat,lon,m=0.08): return bb[1]-m<=lat<=bb[3]+m and bb[0]-m<=lon<=bb[2]+m
def fl(x):
    try: return float(str(x).replace(',','.').split('(')[0])
    except: return None
# ---- estaciones AEMET: normales y mensuales de todos los ficheros disponibles en _ref/aemet
norm={}; mens={}
for f in os.listdir(ref('aemet')):
    d=json.load(open(ref('aemet/'+f),encoding='utf-8'))
    if f.startswith('normales'): norm.update(d)
    if f.startswith('mensuales'):
        for k,v in d.items(): mens[k]={'nombre':v['nombre'],'alt':v['alt'],'lat':v.get('lat'),'lon':v.get('lon'),'rows':v.get('rows',v if isinstance(v,list) else [])} if isinstance(v,dict) else {'rows':v}
EST={e['indicativo']:e for e in json.load(open(ref('aemet/estaciones_canarias.json'),encoding='utf-8'))} if os.path.exists(ref('aemet/estaciones_canarias.json')) else {}
try: EST.update({e['indicativo']:e for e in json.load(open(ref('aemet/estaciones_tenerife.json'),encoding='utf-8'))})
except Exception: pass
def meta(k,v):
    e=EST.get(k,{}); lat=v.get('lat') or e.get('latitud'); lon=v.get('lon') or e.get('longitud'); alt=v.get('alt') or int(e.get('altitud',0)); nombre=v.get('nombre') or e.get('nombre',k)
    return nombre,int(alt),(dms(lat) if lat else None),(dms(lon) if lon else None)
def de_normales(k,v):
    by={int(r['mes']):r for r in v['normales']}; a=by.get(13,{})
    tmm=[fl(by[m]['tm_mes_md']) if m in by else None for m in range(1,13)]
    if a.get('tm_mes_md') in (None,'') or any(t is None for t in tmm): return None
    mf=min(range(12),key=lambda i:tmm[i])+1; mc=max(range(12),key=lambda i:tmm[i])+1
    return dict(tm=fl(a['tm_mes_md']),tf=tmm[mf-1],tn=fl(by[mf]['tm_min_md']),tc=tmm[mc-1],tamin=fl(by[mf]['ta_min_md']),p=fl(a['p_mes_md']),n=fl(a.get('tm_mes_n')),src='AEMET normales 1991-2020',peso=3)
def de_mensuales(k,v):
    mon={}
    for r in v['rows']:
        y,m=r['fecha'].split('-')
        if m!='13': mon[(int(y),int(m))]=r
    years=sorted(set(y for y,m in mon))
    def complete(key): return [y for y in years if 2009<=y and all((y,m) in mon and fl(mon[(y,m)].get(key)) is not None for m in range(1,13))]
    yT=complete('tm_mes'); yP=complete('p_mes')
    def mm(key,yrs,m):
        vals=[fl(mon[(y,m)][key]) for y in yrs if (y,m) in mon and fl(mon[(y,m)].get(key)) is not None]; return st.mean(vals) if vals else None
    o={}
    if len(yT)>=4:
        tmm=[mm('tm_mes',yT,m) for m in range(1,13)]; mf=min(range(12),key=lambda i:tmm[i])+1; mc=max(range(12),key=lambda i:tmm[i])+1
        o.update(tm=st.mean(tmm),tf=tmm[mf-1],tn=mm('tm_min',yT,mf),tc=tmm[mc-1],tamin=mm('ta_min',yT,mf),nT=len(yT))
    if len(yP)>=5: o['p']=sum(mm('p_mes',yP,m) for m in range(1,13)); o['nP']=len(yP)
    return o or None
T=[]; Pp=[]; usadas=[]
# sesgo de las series cortas frente a las normales, con todas las estaciones canarias que tienen ambas
bias=[]
for k,v in norm.items():
    n=de_normales(k,v); m=de_mensuales(k,mens[k]) if k in mens else None
    if n and m and m.get('tm') is not None: bias.append(m['tm']-n['tm'])
BIAS=round(float(np.mean(bias)),2) if bias else 0.4
for k in set(norm)|set(mens):
    v=norm.get(k) or mens.get(k); nombre,alt,lat,lon=meta(k,v)
    if lat is None or not inbox(lat,lon): continue
    vert='N' if lado_norte(C,lon,lat) else 'S'
    n=de_normales(k,norm[k]) if k in norm else None
    m=de_mensuales(k,mens[k]) if k in mens else None
    if n and n['tm'] is not None:
        T.append(dict(src=n['src'],nombre=nombre,alt=alt,vert=vert,tm=n['tm'],tf=n['tf'],tn=n['tn'],tc=n['tc'],tamin=n['tamin'],peso=3)); 
        if n['p'] is not None: Pp.append(dict(src=n['src'],nombre=nombre,alt=alt,vert=vert,p=n['p']))
        usadas.append(f"{k} {nombre} ({alt} m): normales 1991-2020")
    elif m:
        if m.get('tm') is not None: T.append(dict(src='AEMET medias 2009-2025 (−sesgo)',nombre=nombre,alt=alt,vert=vert,tm=m['tm']-BIAS,tf=m['tf']-BIAS,tn=(m['tn']-BIAS if m['tn'] is not None else None),tc=m['tc']-BIAS,tamin=(m['tamin']-BIAS if m['tamin'] is not None else None),peso=2))
        if m.get('p') is not None: Pp.append(dict(src='AEMET medias 2009-2025',nombre=nombre,alt=alt,vert=vert,p=m['p']))
        usadas.append(f"{k} {nombre} ({alt} m): medias {m.get('nT',0)} años T, {m.get('nP',0)} años P")
# ---- Agrocabildo (solo Tenerife)
if C['slug']=='tenerife' and os.path.isdir(ref('agrocabildo')):
    COMARCA_N=['COMARCA DE ACENTEJO','VALLE DE LA OROTAVA','COMARCA DE ICODEN','COMARCA DE DAUTE']
    for r in csv.DictReader(open(ref('agrocabildo/agrocabildo_temperatura_estaciones_2001-2007.csv'),encoding='utf-8')):
        if fl(r['tmedia']) is None or fl(r['inv']) is None or fl(r['ver']) is None: continue
        T.append(dict(src='Agrocabildo 2001-2007',nombre=r['estacion'],alt=int(r['alt']),vert='N' if r['comarca'] in COMARCA_N else 'S',tm=fl(r['tmedia']),tf=fl(r['inv']),tn=None,tc=fl(r['ver']),tamin=None,peso=1))
    NORTE=['ACENTEJO','OROTAVA','ICODEN','DAUTE','ANAGA - TRANSECTO NORESTE','ANAGA - TRANSECTO NOROESTE']
    for r in csv.DictReader(open(ref('agrocabildo/agrocabildo_transectos_lluvia_1983-2010.csv'),encoding='utf-8')):
        vals=[fl(r[k]) for k in ('p1983','p1990','p2000') if fl(r[k]) is not None]
        if vals: Pp.append(dict(src='Agrocabildo 1983-2010',nombre=r['estacion'],alt=int(r['alt']),vert='N' if any(k in r['comarca'] for k in NORTE) else 'S',p=float(np.mean(vals))))
    usadas.append('Agrocabildo: 40 estaciones de temperatura (2001-2007) y 224 pluviómetros (1983-2010)')
PISOS=C['pisos']; INV=C.get('inversion_m',1300)
def band(a): return next((i for i,p in enumerate(PISOS) if p[0]<=a<p[1]),len(PISOS)-1)
def fit(pts,key):
    xs=np.array([p['alt'] for p in pts if p.get(key) is not None],float); ys=np.array([p[key] for p in pts if p.get(key) is not None],float); ws=np.array([p['peso'] for p in pts if p.get(key) is not None],float)
    if len(xs)>=3 and np.ptp(xs)>150: a,b=np.polyfit(xs,ys,1,w=np.sqrt(ws)); return float(a),float(b),int(len(xs))
    if len(xs)>=1: return -0.0065,float(np.average(ys+0.0065*xs,weights=ws)),int(len(xs))   # gradiente estándar anclado en la media de las estaciones [APROXIMADO]
    return None
_hf=sorted([(c['tm_mes_frio'],c['horas_frio']) for c in D['clima']])
def horas_frio(t): return float(np.interp(t,[a for a,_ in _hf],[b for _,b in _hf]))
IZ={'tm':10.5,'tf':4.7,'tn':1.4,'tc':18.5,'tamin':-4.1,'alt':2369}   # Izaña, para la cumbre por encima de la inversión (solo islas que la superan)
clima=[]; ajuste={}; lluvia_tab={}; notas=[]; lreg_regional=False
for v in ['N','S']:
    pts=[p for p in T if p['vert']==v and p['alt']<=INV]
    if len(pts)<3: pts=[p for p in T if p['alt']<=INV]; notas.append(f'vertiente {v}: menos de 3 estaciones de temperatura; regresión con todas las de la isla')
    co={k:fit(pts,k) for k in ['tm','tf','tn','tc','tamin']}
    for k in co:
        if co[k] is None: co[k]=fit([p for p in T],k) or (-0.0065,{'tm':20.5,'tf':17.5,'tn':14.5,'tc':24.0,'tamin':11.5}[k],0)
    ajuste[v]={k:{'pendiente_por_100m':round(100*co[k][0],2),'ordenada':round(co[k][1],2),'n':co[k][2]} for k in co}
    pp=[p for p in Pp if p['vert']==v]; pall=Pp
    lx=np.array([p['alt'] for p in pall],float); ly=np.log(np.array([max(p['p'],20) for p in pall],float))
    lreg=np.polyfit(lx,ly,1) if len(pall)>=3 and np.ptp(lx)>150 else None
    if lreg is None and pall:   # isla con 1-2 pluviómetros: pendiente regional de Canarias (todas las estaciones AEMET ≤1500 m) anclada en los pluviómetros de la isla [APROXIMADO]
        rx=[];ry=[]
        for k in set(norm)|set(mens):
            vv=norm.get(k) or mens.get(k); _,a_,la_,lo_=meta(k,vv)
            if a_ is None or a_>1500: continue
            n_=de_normales(k,norm[k]) if k in norm else None; m_=de_mensuales(k,mens[k]) if k in mens else None
            p_=(n_ or {}).get('p') if n_ and n_.get('p') is not None else (m_ or {}).get('p')
            if p_ is not None: rx.append(float(a_)); ry.append(float(np.log(max(p_,20))))
        if len(rx)>=10:
            b=np.polyfit(np.array(rx),np.array(ry),1)[0]; a=float(np.mean(ly-b*lx)); lreg=np.array([b,a]); lreg_regional=True
            if v=='N': notas.append(f'lluvia: solo {len(pall)} pluviómetro(s) en la isla; se aplica la pendiente regional de Canarias ({len(rx)} estaciones AEMET ≤1500 m, {100*b:+.2f} ln(mm)/100 m) anclada en los de la isla [APROXIMADO]')
    for i,(lo,hi,nombre,z) in enumerate(PISOS):
        def est(k):
            if z<=INV or C['max_alt']<=INV+200: return round(co[k][0]*z+co[k][1],1)
            y4=co[k][0]*INV+co[k][1]; return round(y4+(IZ[k]-y4)*(z-INV)/(IZ['alt']-INV),1)
        bp=[p['p'] for p in pp if band(p['alt'])==i]; src='mediana de pluviómetros'
        if len(bp)<3:   # franja con pocos pluviómetros: regresión del log de la lluvia sobre la cota, de la vertiente si tiene ≥4 puntos, si no de la isla
            vx=np.array([p['alt'] for p in pp],float); vy=np.log(np.array([max(p['p'],20) for p in pp],float))
            vreg=np.polyfit(vx,vy,1) if len(pp)>=4 and np.ptp(vx)>150 else lreg
            if vreg is not None: bp=[float(np.exp(vreg[0]*z+vreg[1]))]; src='regresión log-lluvia/cota ('+('vertiente' if vreg is not lreg else ('regional anclada' if lreg_regional else 'isla'))+')'
            elif pall: bp=[float(np.median([p['p'] for p in pall]))]; src='mediana de toda la isla'
        ll=int(round(float(np.median(bp)))) if bp else None
        lluvia_tab[f'P{i+1}-{v}']={'n':len([p for p in pp if band(p['alt'])==i]),'mediana':ll,'metodo':src}
        tf=est('tf')
        clima.append({'piso':f'P{i+1}-{v}','nombre':nombre,'cota':f'{lo}-{hi}','z_ref':z,'tm_anual':est('tm'),'tm_mes_frio':tf,'tn_mes_frio':est('tn'),'t_abs_min_est':est('tamin'),'tm_mes_calido':est('tc'),'lluvia_mm':ll,'horas_frio':int(round(horas_frio(tf))),'n_pluviometros':len([p for p in pp if band(p['alt'])==i])})
out_={'clima':clima,'ajuste_temperatura':ajuste,'sesgo_2009_2025_vs_normales':BIAS,'lluvia_por_piso':lluvia_tab,'estaciones_temperatura':T,'estaciones_lluvia':Pp,'estaciones_usadas':usadas,'notas':notas,
      'fuentes':[f"AEMET OpenData, valores climatológicos normales 1991-2020 y series mensuales 2009-2025 ({len([u for u in usadas if u[0]=='C'])} estaciones de {C['nombre']})"]+(['Cabildo de Tenerife, Agrocabildo: Temperatura del aire, análisis 2008; L. M. Santana Pérez (2012), ¿Existe cambio pluviométrico en los últimos 40 años en Tenerife?'] if C['slug']=='tenerife' else []),
      'nota':'Temperaturas por regresión sobre la cota con las estaciones de cada vertiente (barlovento N, sotavento S); lluvia por mediana de los pluviómetros de cada franja. '+' '.join(notas)}
json.dump(out_,open(out(C,'92c_pisos_salida.json'),'w'),ensure_ascii=False,indent=0)
print(C['nombre'],'| estaciones T',len(T),'P',len(Pp),'| sesgo',BIAS); [print('  ',c['piso'],c['nombre'],c['tm_anual'],c['tm_mes_frio'],c['t_abs_min_est'],c['lluvia_mm'],'mm',lluvia_tab[c['piso']]['metodo'],c['n_pluviometros']) for c in clima]

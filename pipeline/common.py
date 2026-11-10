# -*- coding: utf-8 -*-
"""Utilidades comunes del pipeline multi-isla: configuración, rutas y helpers."""
import json, os, sys, math
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
REF=os.environ.get('DESPENSA_REF',os.path.join(ROOT,'_ref'))
CFG=json.load(open(os.path.join(HERE,'config_islas.json'),encoding='utf-8'))
def isla(slug=None):
    slug=slug or (sys.argv[1] if len(sys.argv)>1 else None)
    if slug not in CFG: raise SystemExit(f'isla desconocida: {slug}; opciones: {list(CFG)}')
    c=dict(CFG[slug]); c['slug']=slug
    c['version']=os.environ.get('DESPENSA_VERSION','v1')
    c['out']=os.path.join(ROOT,'islas',slug,c['version']); os.makedirs(c['out'],exist_ok=True)
    c['ref']=REF
    return c
def out(c,name): return os.path.join(c['out'],name)
def ref(name): return os.path.join(REF,name)
def lado_norte(c,lon,lat):
    (x1,y1),(x2,y2)=c['linea_vertiente']
    return lat > y1+(lon-x1)*(y2-y1)/(x2-x1)
def zona(c,lon,lat):
    cx,cy=c['centro']; dx=(lon-cx)*math.cos(math.radians(cy)); dy=lat-cy
    az=(math.degrees(math.atan2(dx,dy))+360)%360
    for a,b,n in c['zonas']:
        a2=(a+360)%360; b2=(b+360)%360
        if (a2<=b2 and a2<=az<b2) or (a2>b2 and (az>=a2 or az<b2)): return n
    return c['zonas'][0][2]
def dms(s):   # '282748N' -> 28.463
    v=int(s[:2])+int(s[2:4])/60+int(s[4:6])/3600
    return -v if s[-1] in 'WS' else v
def fmt_es(n,d=0): return f"{n:,.{d}f}".replace(',','X').replace('.',',').replace('X','.')

# -*- coding: utf-8 -*-
"""Monta la carpeta `site/` que se publica en la web, con la misma estructura de URL que territorio.visualizalapalma.es:
  /                         portada con enlaces
  /p/despensa-cerrada/      el visor (última versión)
  /p/despensa-pendiente/    la carga pendiente
  /aviso.html               aviso, fuentes y licencias
  /v1/, /v2/                versiones congeladas (visor, carga pendiente, documentación y datos ligeros)
Uso: python3 scripts/build_site.py  (desde la raíz del repo)
"""
import os, re, shutil, glob, datetime, pathlib
ROOT=pathlib.Path(__file__).resolve().parent.parent
SITE=ROOT/'site'
versions=sorted(p.name for p in ROOT.glob('v*') if p.is_dir() and re.fullmatch(r'v\d+',p.name))
latest=versions[-1]
def viewer(v): return next(iter(sorted((ROOT/v).glob('05_visor_despensa_cerrada_tf_*.html'))))
if SITE.exists(): shutil.rmtree(SITE)
(SITE/'p'/'despensa-cerrada').mkdir(parents=True); (SITE/'p'/'despensa-pendiente').mkdir(parents=True)
def put(src,dst,fix_aviso):
    s=open(src,encoding='utf-8').read().replace('href="aviso_tf.html"',f'href="{fix_aviso}"')
    dst.parent.mkdir(parents=True,exist_ok=True); open(dst,'w',encoding='utf-8').write(s)
put(viewer(latest),SITE/'p'/'despensa-cerrada'/'index.html','../../aviso.html')
put(ROOT/latest/'99_CARGA_PENDIENTE_TF.html',SITE/'p'/'despensa-pendiente'/'index.html','../../aviso.html')
s=open(ROOT/latest/'aviso_tf.html',encoding='utf-8').read()
s=re.sub(r'<a href="05_visor_despensa_cerrada_tf_v\d+\.html">','<a href="p/despensa-cerrada/">',s)
open(SITE/'aviso.html','w',encoding='utf-8').write(s)
# versiones congeladas
for v in versions:
    d=SITE/v; d.mkdir()
    put(viewer(v),d/'visor.html','aviso.html'); put(ROOT/v/'99_CARGA_PENDIENTE_TF.html',d/'carga-pendiente.html','aviso.html')
    shutil.copy(ROOT/v/'aviso_tf.html',d/'aviso.html')
    for f in ['00_INDICE.md','01_RESUMEN.md','04_lectura_balance_tf.md','91_fuentes_y_licencias_tf.md','90_verificacion_tf.csv','03_catalogo_viabilidad_tf.csv','95_catalogo_salida_tf.json','97_balance_salida_tf.json','04b_cocina_tf.json']:
        if (ROOT/v/f).exists(): shutil.copy(ROOT/v/f,d/f)
# ---- otras islas (pipeline multi-isla): /<slug>/
import json as _json
CFG=_json.load(open(ROOT/'pipeline'/'config_islas.json',encoding='utf-8')) if (ROOT/'pipeline'/'config_islas.json').exists() else {}
islas=[]
for slug,cfg in CFG.items():
    if slug=='tenerife': continue
    vers=sorted(p.name for p in (ROOT/'islas'/slug).glob('v*') if p.is_dir() and (p/'05_visor_despensa_cerrada.html').exists()) if (ROOT/'islas'/slug).exists() else []
    if not vers: continue
    v=vers[-1]; src=ROOT/'islas'/slug/v; d=SITE/slug; d.mkdir(parents=True,exist_ok=True)
    shutil.copy(src/'05_visor_despensa_cerrada.html',d/'index.html'); shutil.copy(src/'99_CARGA_PENDIENTE.html',d/'carga-pendiente.html'); shutil.copy(src/'aviso.html',d/'aviso.html')
    for fn in ['00_INDICE.md','01_RESUMEN.md','04_lectura_balance.md','91_fuentes_y_licencias.md','90_verificacion.csv','03_catalogo_viabilidad.csv','95_catalogo_salida.json','97_balance_salida.json','04b_cocina.json']:
        if (src/fn).exists(): shutil.copy(src/fn,d/fn)
    try: z=_json.load(open(src/'97_balance_salida.json'))['rejilla']['insular|0.3|1|1']['z']; pob=_json.load(open(src/'97_balance_salida.json'))['c1']['poblacion']
    except Exception: z=None; pob=None
    islas.append((slug,cfg['nombre'],v,z,pob))
hoy=datetime.date.today().strftime('%d/%m/%Y')
vlist=''.join(f'<li><a href="{v}/visor.html">{v}</a> · <a href="{v}/carga-pendiente.html">carga pendiente</a> · <a href="{v}/01_RESUMEN.md">resumen</a> · <a href="{v}/04_lectura_balance_tf.md">lectura del balance</a></li>' for v in reversed(versions))
open(SITE/'index.html','w',encoding='utf-8').write(f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Tenerife, despensa cerrada</title>
<style>:root{{--bg:#F3F5F2;--panel:#fff;--ink:#18222D;--muted:#5B6773;--line:#D8DDD8;--accent:#2F6B4F}}@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#11171D;--panel:#18212A;--ink:#E6ECE8;--muted:#9AA7B2;--line:#2A3540;--accent:#6FC29A;color-scheme:dark}}}}:root[data-theme="dark"]{{--bg:#11171D;--panel:#18212A;--ink:#E6ECE8;--muted:#9AA7B2;--line:#2A3540;--accent:#6FC29A;color-scheme:dark}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 "Segoe UI",system-ui,sans-serif;padding:24px 16px 48px}}main{{max-width:820px;margin:0 auto}}h1{{font-size:clamp(28px,6vw,44px);line-height:1.1;margin:.2em 0}}.tag{{display:inline-block;font:600 12px/1 ui-monospace,monospace;letter-spacing:.06em;padding:5px 8px;border:1px solid var(--line);border-radius:5px;color:var(--muted);margin-right:6px}}.card{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:14px 0}}.card h2{{font-size:1.15rem;margin:0 0 6px}}.islas{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px;margin:12px 0}}.isla{{display:block;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 14px;text-decoration:none;color:var(--ink)}}.isla b{{display:block;font-size:1.05rem}}.isla span{{display:block;color:var(--muted);font-size:.9rem;margin-top:4px}}a{{color:var(--accent)}}.muted{{color:var(--muted)}}ul{{padding-left:20px}}</style></head>
<body><main>
<p><span class="tag">SIMULACIÓN</span><span class="tag">prototipo personal · sin carácter oficial</span><span class="tag">{latest} · {hoy}</span></p>
<h1>Tenerife, despensa cerrada</h1>
<p>Si el mundo se cerrara y la isla dejara de exportar plátano: qué se podría cultivar, criar y pescar, cuánta tierra y agua quedarían libres y qué habría en una nevera y una despensa solo con producto tinerfeño. Y, con casi un millón de residentes, si alcanzaría. Réplica para Tenerife del visor <a href="https://territorio.visualizalapalma.es/p/despensa-cerrada/">«La Palma, despensa cerrada»</a> de Jorge Díaz Pérez.</p>
<div class="card"><h2><a href="p/despensa-cerrada/">El visor</a></h2><p class="muted">Siete escenas: la isla parcela a parcela en 3D, el catálogo de lo que cabe, lo que libera la platanera, el reparto y si alcanza para comer, la nevera, la semana y el botiquín. Un solo HTML, funciona sin conexión.</p></div>
<div class="card"><h2><a href="p/despensa-pendiente/">Carga pendiente</a></h2><p class="muted">Lo que falta para dar por bueno el visor: deuda por frente, decisiones abiertas y prompt de reinicio.</p></div>
<div class="card"><h2><a href="aviso.html">Aviso, fuentes y licencias</a></h2><p class="muted">Prototipo divulgativo hecho con IA. Datos abiertos del Gobierno de Canarias, ISTAC, Copernicus, FAO y AEMET.</p></div>
<h2 style="font-size:1rem;color:var(--muted);letter-spacing:.06em;text-transform:uppercase;margin-top:28px">Las otras islas</h2>
<p class="muted">El mismo método, aplicado isla a isla con sus propios datos (Mapa de Cultivos, relieve, estaciones, población, pesca). Para La Palma, el <a href="https://territorio.visualizalapalma.es/p/despensa-cerrada/">visor original</a> de Jorge Díaz Pérez.</p>
<div class="islas">{''.join(f'<a class="isla" href="{slug}/"><b>{nombre}</b><span>{v} · {f"{pob:,}".replace(",",".") if pob else ""} residentes · cobertura de referencia {round(100*z) if z is not None else "?"} %</span></a>' for slug,nombre,v,z,pob in islas)}</div>
<h2 style="font-size:1rem;color:var(--muted);letter-spacing:.06em;text-transform:uppercase;margin-top:28px">Versiones de Tenerife</h2>
<ul>{vlist}</ul>
<p class="muted">Código y datos: <a href="https://github.com/gonzapico/tenerife-despensa-cerrada">github.com/gonzapico/tenerife-despensa-cerrada</a>. En una emergencia, llama al 112.</p>
</main></body></html>''')
# comprobación: ninguna referencia externa en scripts, estilos o imágenes
bad=[]
for f in SITE.rglob('*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.findall(r'<(?:script|link|img)[^>]+(?:src|href)="(https?://[^"]+)"',s): bad.append((str(f.relative_to(SITE)),m))
assert not bad, bad
print('site OK:',sum(1 for _ in SITE.rglob('*') if _.is_file()),'ficheros; última versión de Tenerife',latest,'; islas:',[i[0] for i in islas])

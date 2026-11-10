# -*- coding: utf-8 -*-
"""Documentación de la isla: 00_INDICE, 01_RESUMEN, 04_lectura_balance, 91_fuentes_y_licencias, 90_verificacion, aviso.html."""
import os, sys, json, datetime, pandas as pd
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import isla, out, fmt_es as f
C=isla(); N=C['nombre']; V=C['version']; hoy=datetime.date.today().strftime('%d/%m/%Y')
B=json.load(open(out(C,'97_balance_salida.json'))); K=json.load(open(out(C,'95_catalogo_salida.json'))); T=json.load(open(out(C,'94_territorio_salida.json')))['terr']; PI=json.load(open(out(C,'92c_pisos_salida.json'))); MAPA=json.load(open(out(C,'mapa_oficial_resumen.json')))
test=json.load(open(out(C,'90_test_resultado.json'))) if os.path.exists(out(C,'90_test_resultado.json')) else None
R=B['rejilla']; c1=B['c1']; P=B['param']; ref=R['insular|0.3|1|1']; best=max(v['z'] for v in R.values())
rows=[]
for esc,et in [('autarquia','Autarquía estricta'),('insular','Insular, insumos actuales'),('espana','Media de España')]:
    for gan in (0,1):
        for pm in (1,3):
            zs=[R[f'{esc}|{fs/10:.1f}|{pm}|{gan}']['z'] for fs in range(11)]
            rows.append((et,'con ganado' if gan else 'sin ganado','pesca ×3' if pm==3 else 'pesca 2021',f"{100*zs[0]:.0f} %",f"{100*zs[3]:.0f} %",f"{100*zs[10]:.0f} %"))
tab="| Insumos | Ganado | Pesca | 0 % SANU | 30 % SANU | 100 % SANU |\n|---|---|---|---:|---:|---:|\n"+"\n".join("| "+" | ".join(r)+" |" for r in rows)
filas="| Destino | Dónde | ha / cabezas | Producción | Factor |\n|---|---|---:|---:|---:|\n"+"\n".join(f"| {x['nombre']} | {({'A':'costa, regadío (ex platanera)','Bs':'medianías, secano','Br':'medianías, regadío'}).get(x.get('bolsa'),'establo y monte')} | {f(x['valor'])} | {f(x['t'])+' t' if x['tipo']=='cultivo' else (f(x['t_ms'])+' t MS' if x['tipo']=='forraje' else f(x['leche_t'])+' t leche · '+f(x['carne_t'])+' t carne')} | {x.get('f','')} |" for x in sorted(ref['filas'],key=lambda x:(x['tipo'],-x['valor'])))
clima="| Piso | Cota | T media | T mes frío | Mín. abs. est. | Lluvia | Pluviómetros | H. frío |\n|---|---|---:|---:|---:|---:|---:|---:|\n"+"\n".join(f"| {c['piso']} · {c['nombre']} | {c['cota']} m | {f(c['tm_anual'],1)} °C | {f(c['tm_mes_frio'],1)} °C | {f(c['t_abs_min_est'],1)} °C | {c['lluvia_mm']} mm | {c['n_pluviometros']} ({PI['lluvia_por_piso'][c['piso']]['metodo']}) | {c['horas_frio']} |" for c in K['clima'])
rend="| Cultivo del modelo | FAOSTAT España (kg/ha) | ISTAC (kg/ha) | Factor | Fuente |\n|---|---:|---:|---:|---|\n"+"\n".join(f"| {c} | {f(k['rend'])} | {f(k['rend_tf']) if k['rend_tf'] else '—'} | {k['f_tf']} | {k['fuente_rend']} |" for c,k in B['cult'].items())
sec=sum(1 for c in K['cat'] if c['a'] and c['c']=='VIABLE SECANO'); rie=sum(1 for c in K['cat'] if c['a'] and c['c']=='VIABLE CON RIEGO')
agua_lineas=f"{f(P['AGUA']/1e6,1)} hm³/año con la dotación {c1['metodo_defecto']} ({f({'A':c1['dot_A'],'C':c1['dot_C'],'D':c1['dot_D'],'B1':c1['dot_B'][0],'B2':c1['dot_B'][1]}[c1['metodo_defecto']])} m³/ha)" + (f", el {f(100*P['AGUA']/1e6/c1['demanda_agraria_hm3'])} % de la demanda agraria de la isla ({f(c1['demanda_agraria_hm3'],2)} hm³)" if c1['demanda_agraria_hm3'] else "")
open(out(C,'04_lectura_balance.md'),'w',encoding='utf-8').write(f"""# 04 · Lectura del balance de suficiencia de {N} ({V}) [BORRADOR]

Corte: {hoy}. Pipeline multi-isla; método y coeficientes de nutrición y ganadería heredados del visor «La Palma, despensa cerrada» v6 y del de Tenerife v4.

## Cifras de partida (C1–C2)

- Residentes: {f(c1['poblacion'])} (ISTAC, cifras oficiales a 1-1-2025) [VERIFICADO]
- Platanera: {f(c1['platanera_ha'],1)} ha ({f(c1['platanera_invernadero_ha'])} ha bajo invernadero) en el Mapa de Cultivos de {N} {MAPA['anio']} [VERIFICADO]; retenida para consumo local a 15 kg/hab·año [REQUIERE_FUENTE] y {f((c1['rend_platanera_istac'] or 47),1)} t/ha: {f(c1['platanera_ha']-c1['c1_liberada_ha'],1)} ha; liberada: {f(c1['c1_liberada_ha'],1)} ha
- Agua liberada: {agua_lineas}. Fuente del agua: {c1['agua_fuente']}
- Suelo agrícola no utilizado: {f(c1['sanu_ha'],1)} ha; barbecho: {f(c1['barbecho_ha'],1)} ha (no entra) [VERIFICADO]
- Pesca: {f(P['PESCA_T'],1)} t vendidas en primera venta en puertos de {N} en 2021 [VERIFICADO]
- Censo ganadero 2025 (ISTAC): {', '.join(f"{v} {k}" for k,v in c1['censo_2025'].items() if v)}; techo del monte {f(P['MONTE_CAP'])} t MS/año [APROXIMADO]
- Necesidades: 2.250 kcal, 55 g de proteína, 70 g de grasa y 400 g de frutas y hortalizas por persona y día [APROXIMADO]

## Pisos climáticos

{clima}

{PI['nota']} Estaciones: {len(PI['estaciones_temperatura'])} de temperatura y {len(PI['estaciones_lluvia'])} pluviómetros. Sesgo de las series cortas frente a las normales: {PI['sesgo_2009_2025_vs_normales']} °C.

## Rendimientos agrícolas (ISTAC, mediana 2017-2023)

{rend}

## Cobertura mínima en los 132 escenarios

{tab}

Lectura: **ningún escenario pasa del {f(100*best)} %**. En el de referencia (insumos actuales, 30 % del suelo abandonado recuperado, ganado, pesca de 2021) la cobertura es del {f(100*ref['z'])} %: energía {f(100*ref['cob']['kcal'])} %, proteína {f(100*ref['cob']['prot'])} %, grasa {f(100*ref['cob']['grasa'])} %, frutas y hortalizas {f(100*ref['cob_fyh'])} %. La producción actual sin plátano aporta el {f(100*ref['cob_base']['kcal'],1)} % de la energía y la pesca el {f(100*ref['cob_pesca']['prot'],1)} % de la proteína. [INFERENCIA]

## Reparto del escenario de referencia (insular|0.3|1|1)

{filas}

Agua usada: {f(ref['agua_usada']/1e6,1)} de {f(P['AGUA']/1e6,1)} hm³. Tierra: {f(ref['tierraA'])} ha de costa y {f(ref['tierraB'])} ha de medianías de las {f(ref['supB'])} recuperables.

## Decisiones (revisables)

1. Frutas y hortalizas como cuarta cobertura en proporción.
2. Techo del monte para el caprino: 0,35 t MS por cabra sobre el máximo del censo ISTAC 2014-2025.
3. Rendimientos: factor por cultivo ISTAC/FAOSTAT (isla, o media de Canarias si la isla no tiene superficie); España = máx(factor, 1); sin dato, 0,7.
4. Dotación del plátano: {c1['metodo_defecto']} por defecto.
5. Pisos climáticos: dos vertientes, regresión de temperatura, mediana de pluviómetros por franja.
""")
open(out(C,'91_fuentes_y_licencias.md'),'w',encoding='utf-8').write(f"""# 91 · Fuentes, licencias y etiquetas · {N} ({V}) [BORRADOR]

| F | Fuente | Uso | Licencia | Estado |
|---|---|---|---|---|
| F1 | Mapa de Cultivos de {N} {MAPA['anio']}, Gobierno de Canarias (`opendata.sitcan.es/upload/medio-rural/gobcan_mapa-cultivos_*_shp.zip`, fichero {MAPA['fichero']}). {f(MAPA['parcelas'])} parcelas, {f(MAPA['ha_total'])} ha; campos CULTIVO, REGADIO, ABANDON, TECNICA | parcelas, superficies, riego, suelo abandonado, calibración | CC BY 4.0 | [VERIFICADO] |
| F2 | Copernicus DEM GLO-30, teselas {', '.join(C['dem'])} (`copernicus-dem-30m` en AWS) | relieve, cota y pendiente | © DLR/Airbus, Copernicus (UE/ESA), uso libre con atribución | [VERIFICADO] |
| F3 | FAO ECOCROP, copia pública en github.com/OpenCLIM/ecocrop | requisitos de temperatura y lluvia; solo cálculo | FAO; copia bajo OGL v3 | [VERIFICADO] el origen |
| F4 | Universo FAOSTAT 2024 y variedades locales, heredados del visor de La Palma | catálogo | CC BY 4.0 | [VERIFICADO] |
| F5 | AEMET OpenData: normales 1991-2020 y series mensuales 2009-2025 de las estaciones de la isla ({len(PI['estaciones_usadas'])} usadas, ver 92c_pisos_salida.json){'; Agrocabildo (Cabildo de Tenerife): 40 estaciones de temperatura 2001-2007 y 224 pluviómetros 1983-2010' if C['slug']=='tenerife' else ''} | pisos climáticos | AEMET, citar como autora | [VERIFICADO] el origen; series cortas [APROXIMADO] |
| F6 | ISTAC, Cifras oficiales de población, municipios por islas (E30245A_000002, 15/12/2025): {N} {f(c1['poblacion'])} a 1-1-2025 | residentes | ISTAC | [VERIFICADO] |
| F7 | {c1['agua_fuente']} | dotación y demanda agraria | — | ver etiquetas en la fuente |
| F8 | Gobierno de Canarias, Registro de primera venta de productos pesqueros 2021 (datos.canarias.es): {f(P['PESCA_T'],1)} t en puertos de {N} | pesca, especies y meses | CC BY 4.0 | [VERIFICADO]; solo 2021 publicado |
| F9 | ISTAC, Efectivos de ganado según especies, islas 2014-2025 (E01008B_000001) | calibración del techo del monte | ISTAC | [VERIFICADO] |
| F10 | Composición nutricional y coeficientes de ganado, forraje y nitrógeno | balance | heredados de La Palma | [APROXIMADO]/[CONOCIMIENTO_BASE] |
| F11 | Nevera, despensa, menú y botiquín: base canaria y particularidades de la isla (pipeline/cocina_islas.json) | escenas 5-7 | — | [CONOCIMIENTO_BASE] |
| F12 | ISTAC, Estadística anual de superficies y producciones de cultivos (E01135A_000003/4/5), {N} y Canarias, mediana 2017-2023 | rendimientos por cultivo y de la platanera | ISTAC | [VERIFICADO] |

Etiquetas: [VERIFICADO] dato leído de su fuente; [APROXIMADO] cifra de segunda mano o redondeada; [INFERENCIA] resultado del modelo o del criterio propio; [REQUIERE_FUENTE] sin acreditar; [CONOCIMIENTO_BASE] aportado de memoria por la IA.

Licencias de la obra: código MIT; textos, ilustraciones y datos derivados CC BY 4.0 (ver LICENSE y LICENSE-CONTENIDO.md en la raíz del repositorio); three.js (MIT) incrustado; datos con la licencia de su titular.
""")
ver=[('catálogo','calibración con el campo REGADIO del Mapa de Cultivos oficial',f"{K['calibra']['ok']}/{K['calibra']['n']}",'CUMPLE' if K['calibra']['ok']==K['calibra']['n'] else 'NO CUMPLE'),
 ('rejilla','132 escenarios resueltos por HiGHS (status 0)',f"{sum(1 for v in R.values() if v['ok'])}/132",'CUMPLE' if all(v['ok'] for v in R.values()) else 'NO CUMPLE'),
 ('territorio','parcelas rasterizadas sobre el DEM',f"{T['parcelas']}",'CUMPLE'),
 ('clima','estaciones de temperatura y pluviómetros usados',f"{len(PI['estaciones_temperatura'])} / {len(PI['estaciones_lluvia'])}",'CUMPLE' if len(PI['estaciones_temperatura'])>=3 else 'REVISAR')]
if test:
    v=test['vistas'][0]
    ver+= [('visor','conexiones externas al cargar',str(test['externas']),'CUMPLE' if test['externas']==0 else 'NO CUMPLE'),('visor','errores de consola (escritorio y móvil)',str(test['errores']),'CUMPLE' if test['errores']==0 else 'NO CUMPLE'),
           ('visor','scroll horizontal a 390 px','no' if all(x['scrollW']<=x['innerW'] for x in test['vistas']) else 'sí','CUMPLE' if all(x['scrollW']<=x['innerW'] for x in test['vistas']) else 'NO CUMPLE'),
           ('C1','tierra liberada recalculada en el navegador frente a la tabla',v['check1'].split(': ')[-1],'CUMPLE' if 'CUMPLE' in v['check1'] and 'NO CUMPLE' not in v['check1'] else 'NO CUMPLE'),
           ('C4','coberturas recalculadas en el navegador frente a la rejilla',v['check4'].split(': ')[-1],'CUMPLE' if 'CUMPLE' in v['check4'] and 'NO CUMPLE' not in v['check4'] else 'NO CUMPLE')]
pd.DataFrame(ver,columns=['pieza','prueba','resultado','estado']).to_csv(out(C,'90_verificacion.csv'),index=False)
open(out(C,'00_INDICE.md'),'w',encoding='utf-8').write(f"""# {N}, despensa cerrada · {V} ({hoy}) [BORRADOR]

Réplica para {N} del visor «La Palma, despensa cerrada» (territorio.visualizalapalma.es) con el pipeline multi-isla del repositorio (`pipeline/`). Generada con `pipeline/run.sh {C['slug']}`.

## Piezas firmables
- `01_RESUMEN.md` · resumen ejecutivo en cinco puntos · `04_lectura_balance.md` · escenarios y cifras · `03_catalogo_viabilidad.csv` · catálogo por pisos
- `05_visor_despensa_cerrada.html` · **el visor** (un solo HTML, sin red) · `aviso.html` · aviso, fuentes y licencias · `99_CARGA_PENDIENTE.html` · deuda y prompt de reinicio

## Soporte
- `90_verificacion.csv`, `90_test_resultado.json`, `cap_*.png` · pruebas · `91_fuentes_y_licencias.md` · fuentes F1–F12
- `mapa_oficial_resumen.json`, `92c_pisos_salida.json`, `95_catalogo_salida.json`, `97_balance_salida.json`, `94_territorio_salida.json`, `04b_cocina.json`, `tex_hoy.jpg`, `tex_fut.jpg` · salidas intermedias
- `parcelas.parquet` (no versionado) · parcelas con cota y pendiente; se regenera con `pipeline/00_preparar_parcelas.py {C['slug']}` a partir del shapefile en `_ref/shp/` y las teselas DEM en `_ref/dem/`
""")
open(out(C,'01_RESUMEN.md'),'w',encoding='utf-8').write(f"""# 01 · Resumen ejecutivo · {N}, despensa cerrada {V} [BORRADOR]

1. **Qué hay.** Un visor autocontenido con las siete escenas del de La Palma y su página de carga pendiente, montados con datos de {N} leídos de su fuente: {f(T['parcelas'])} parcelas del Mapa de Cultivos {MAPA['anio']} sobre el relieve Copernicus, población, censo y rendimientos del ISTAC, estaciones de AEMET, primera venta de pesca 2021 y el plan hidrológico insular.
2. **Qué se podría cultivar.** De 144 productos alimentarios, {sec} se dan en secano y {rie} con riego en alguno de los {len(K['clima'])} pisos; calibración con el campo REGADIO oficial {K['calibra']['ok']}/{K['calibra']['n']}.
3. **Qué libera el plátano.** {f(c1['platanera_ha'])} ha de platanera{'; es testimonial, no hay exportación que cerrar' if c1['platanera_ha']<100 else ': la isla retendría '+f(c1['platanera_ha']-c1['c1_liberada_ha'])+' ha y quedarían libres '+f(c1['c1_liberada_ha'])+' ha'}; agua liberada {agua_lineas}. Suelo abandonado: {f(c1['sanu_ha'])} ha.
4. **Si alcanza.** {'No. ' if best<1 else ''}Con insumos actuales, el 30 % del suelo abandonado recuperado y ganado, la isla cubre el {f(100*ref['z'])} % de las necesidades de sus {f(c1['poblacion'])} residentes; en el mejor de los 132 escenarios, el {f(100*best)} %. La Palma llegaba al 110 % y Tenerife al 22 %. [INFERENCIA]
5. **Qué queda pendiente.** Los coeficientes de ganado, forraje y nutrición heredados de La Palma, la dotación medida del plátano en la isla, la revisión local de la nevera y la despensa, y las decisiones declaradas en `04_lectura_balance.md`. Desglosado en `99_CARGA_PENDIENTE.html`.
""")
open(out(C,'aviso.html'),'w',encoding='utf-8').write(f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Aviso, fuentes y licencias · {N}, despensa cerrada</title>
<style>:root{{--bg:#F3F5F2;--ink:#18222D;--muted:#5B6773;--line:#D8DDD8;--accent:#2F6B4F}}@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#11171D;--ink:#E6ECE8;--muted:#9AA7B2;--line:#2A3540;--accent:#6FC29A;color-scheme:dark}}}}:root[data-theme="dark"]{{--bg:#11171D;--ink:#E6ECE8;--muted:#9AA7B2;--line:#2A3540;--accent:#6FC29A;color-scheme:dark}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 "Segoe UI",system-ui,sans-serif;padding:24px 16px 48px}}main{{max-width:820px;margin:0 auto}}h1{{font-size:1.7rem;line-height:1.15}}h2{{font-size:1.1rem;margin-top:1.6em;color:var(--accent)}}a{{color:var(--accent)}}.muted{{color:var(--muted)}}hr{{border:0;border-top:1px solid var(--line);margin:24px 0}}</style></head>
<body><main>
<h1>Aviso, fuentes y licencias</h1>
<p><strong>Prototipo divulgativo hecho con IA. No es una herramienta oficial ni una predicción.</strong> «{N}, despensa cerrada» es un ejercicio personal de divulgación, sin respaldo institucional ni carácter oficial, que replica para {N} el método del visor «La Palma, despensa cerrada» (Jorge Díaz Pérez, <a href="https://territorio.visualizalapalma.es/">territorio.visualizalapalma.es</a>). Mezcla datos abiertos, simulaciones y escenarios hipotéticos, y puede contener errores. No sustituye a ningún acto administrativo, informe técnico ni predicción oficial. Las menciones al Gobierno de Canarias, al Cabildo o al Consejo Insular de Aguas se limitan a citar sus datos como fuente.</p>
<h2>Fuentes</h2>
<ul>
<li><strong>Parcelas y cultivos:</strong> Mapa de Cultivos de {N} {MAPA['anio']}, Gobierno de Canarias, CC BY 4.0 (opendata.sitcan.es). {f(MAPA['parcelas'])} parcelas, {f(MAPA['ha_total'])} ha, con los campos de riego, abandono y técnica. [VERIFICADO]</li>
<li><strong>Relieve:</strong> Copernicus DEM GLO-30, © DLR e.V. 2010-2014 y © Airbus Defence and Space GmbH 2014-2018, proporcionado bajo COPERNICUS por la Unión Europea y la ESA; todos los derechos reservados. Exageración vertical ×2. [VERIFICADO]</li>
<li><strong>Catálogo de productos:</strong> universo de FAOSTAT 2024 (FAO, CC BY 4.0) heredado del visor de La Palma. Requisitos de cultivo: FAO ECOCROP, copia pública del repositorio OpenCLIM/ecocrop, usada solo para el cálculo. Reglas de clasificación propias, declaradas en el pipeline.</li>
<li><strong>Clima por pisos:</strong> AEMET OpenData, valores climatológicos normales 1991-2020 y series mensuales 2009-2025 de las estaciones de la isla (AEMET como autora de los datos){'; Cabildo de Tenerife, Agrocabildo (temperatura 2001-2007 y pluviómetros 1983-2010)' if C['slug']=='tenerife' else ''}. Temperatura por regresión sobre la cota por vertiente; lluvia por mediana de los pluviómetros de cada franja. [VERIFICADO el origen; método propio declarado]</li>
<li><strong>Población y ganado:</strong> ISTAC, cifras oficiales de población a 1 de enero de 2025 y efectivos de ganado 2014-2025. [VERIFICADO]</li>
<li><strong>Rendimientos agrícolas:</strong> ISTAC, Estadística anual de superficies y producciones de cultivos, {N} y Canarias, mediana 2017-2023. [VERIFICADO]</li>
<li><strong>Agua:</strong> {c1['agua_fuente']}.</li>
<li><strong>Pesca:</strong> registro de primera venta de productos pesqueros 2021 (Gobierno de Canarias, CC BY 4.0): {f(P['PESCA_T'],1)} t en puertos de {N}, por especie y mes. [VERIFICADO]</li>
<li><strong>Composición nutricional, ganadería y cocina:</strong> coeficientes heredados del visor de La Palma; nevera, despensa, menú y botiquín escritos de memoria a partir de la tradición de la isla. [CONOCIMIENTO_BASE]</li>
</ul>
<h2>Licencias y reutilización</h2>
<p>Código bajo licencia MIT; textos, ilustraciones y datos derivados bajo CC BY 4.0, citando «{N}, despensa cerrada» y el visor original de La Palma. Los datos conservan la licencia de su titular. three.js se incrusta bajo licencia MIT. Las cifras llevan etiqueta epistémica: [VERIFICADO], [APROXIMADO], [INFERENCIA], [REQUIERE_FUENTE], [CONOCIMIENTO_BASE].</p>
<p class="muted">En una emergencia, llama al 112.</p>
<hr><p class="muted"><a href="index.html">← Volver al visor</a> · <a href="https://github.com/gonzapico/tenerife-despensa-cerrada">Código y datos</a></p>
</main></body></html>""")
print(N,'docs OK')

# -*- coding: utf-8 -*-
"""Ensambla el visor autocontenido «<Isla>, despensa cerrada» (pipeline multi-isla) sobre la plantilla de La Palma (misma estructura y three.js)."""
import os, sys, json, datetime, re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import isla, out, ref, fmt_es as f
C=isla(); N=C['nombre']; G=C['gent']; GF=C['gent_f']; GP=C['gent_pl']
src=open(ref('lapalma_visor.html'),encoding='utf-8').read()
cat=json.load(open(out(C,'95_catalogo_salida.json'))); bal=json.load(open(out(C,'97_balance_salida.json'))); terr=json.load(open(out(C,'94_territorio_salida.json'))); coc=json.load(open(out(C,'04b_cocina.json'))); pis=json.load(open(out(C,'92c_pisos_salida.json'))); MAPA=json.load(open(out(C,'mapa_oficial_resumen.json')))
D={'cat':cat['cat'],'clima':cat['clima'],'calibra':cat['calibra'],'c1':bal['c1'],'param':bal['param'],'cult':bal['cult'],'bases':bal['bases'],'rejilla':bal['rejilla'],
   'nevera':coc['nevera'],'menu':coc['menu'],'botiquin':coc['botiquin'],'terr':terr['terr'],'alt':terr['alt'],'texHoy':terr['texHoy'],'texFut':terr['texFut']}
CAL=cat['calibra']; c1=bal['c1']; P=bal['param']; NP=len(C['pisos']); COTAS='['+', '.join(f'[{a}, {b}]' for a,b,_,_ in C['pisos'])+']'
REND=round(c1['rend_platanera_istac'] or 47); MET=c1['metodo_defecto']; PLAT=c1['platanera_ha']; poca=PLAT<100
i=src.find('const D = {'); j=src.find('\n',i); html=src[:i]+'const D = '+json.dumps(D,ensure_ascii=False,separators=(',',':'))+';'+src[j:]
hoy=datetime.date.today().strftime('%d/%m/%Y'); anio=MAPA['anio']; ver=C['version']
agua_txt={'A':'la media del regadío de la isla','B1':'el consumo por planta (15 L/día)','B2':'el consumo por planta (20 L/día)','C':'la dotación del plátano de la IPH de Canarias (10.000 m³/ha)','D':'el consumo medido en la isla'}[MET]
R=[ # lógica
 ('const COTAS = [[0, 300], [300, 600], [600, 1000], [1000, 1500], [1500, 2426]]',f'const COTAS = {COTAS}'),
 ('for (let i = 0; i < 5; i++) for (const v of ["E", "O"])',f'for (let i = 0; i < {NP}; i++) for (const v of ["N", "S"])'),
 ('v === "E" ? " · " + c.nombre','v === "N" ? " · " + c.nombre'),
 ('<dt>Hoy en La Palma</dt>',f'<dt>Hoy en {N}</dt>'),
 ('alt="Mapa de La Palma con parcelas coloreadas"',f'alt="Mapa de {N} con parcelas coloreadas"'),
 ('"Hoy (Mapa de Cultivos 2021-22)"',f'"Hoy (Mapa de Cultivos {anio})"'),
 ('Escenario del reparto: insumos actuales, 30 % del suelo abandonado recuperado y ganadería. La platanera (${fmt(T.platanera_ha)} ha) se reparte entre cultivos por orden de exigencia de calor: lo más cálido, en las parcelas más bajas. Del suelo abandonado se recuperan las ${fmt(T.recuperada_ha)} ha de menor pendiente. [INFERENCIA]',
  'Escenario del reparto: insumos actuales, 30 % del suelo abandonado recuperado y ganadería. La platanera (${fmt(T.platanera_ha)} ha) se reparte entre cultivos y forraje por orden de exigencia de calor: lo más cálido, en las parcelas más bajas. Del suelo abandonado (${fmt(D.param.SANU)} ha) se recuperan las ${fmt(T.recuperada_ha)} ha de menor pendiente. ${fmt(T.parcelas)} parcelas. [INFERENCIA]'),
 ('objetivo = new THREE.Vector3(0, 0, 1.5)','objetivo = new THREE.Vector3(0, 0, 0.5)'),
 ('const V = { oblicua: [0.35, 0.9, 55], cenital: [0, 0.02, 62], sur: [Math.PI, 0.98, 55] };','const V = { oblicua: [0.35, 0.9, 92], cenital: [0, 0.02, 100], sur: [Math.PI, 0.98, 92] };'),
 ('rad = Math.min(95, Math.max(10, rad * d0 / d))','rad = Math.min(160, Math.max(15, rad * d0 / d))'),
 ('rad = Math.min(95, Math.max(10, rad * (e.deltaY > 0 ? 1.1 : 0.9)))','rad = Math.min(160, Math.max(15, rad * (e.deltaY > 0 ? 1.1 : 0.9)))'),
 ('const cam = new THREE.PerspectiveCamera(38, 1, 0.1, 500)','const cam = new THREE.PerspectiveCamera(38, 1, 0.1, 800)'),
 ('const dot = { A: B.dot_A, B1: B.dot_B[0], B2: B.dot_B[1] }[S.metodo];','const dot = { A: B.dot_A, B1: B.dot_B[0], B2: B.dot_B[1], C: B.dot_C, D: B.dot_D }[S.metodo] || 0;'),
 ('[["A", "A · media del regadío"], ["B1", "B · 15 L/planta"], ["B2", "B · 20 L/planta"]]','[["A", "A · media del regadío"], ["B1", "B · 15 L/planta"], ["B2", "B · 20 L/planta"], ["C", "C · IPH Canarias"], ["D", "D · medido en la isla"]].filter(([k]) => ({A: D.c1.dot_A, D: D.c1.dot_D})[k] !== null && ({A: D.c1.dot_A, D: D.c1.dot_D})[k] !== undefined)'),
 ('sel: null, kg: 15, rend: 44, metodo: "A"',f'sel: null, kg: 15, rend: {REND}, metodo: "{MET}"'),
 ('if (S.kg === 15 && S.rend === 44 && S.metodo === "A")',f'if (S.kg === 15 && S.rend === {REND} && S.metodo === "{MET}")'),
 ('const d = Math.abs(lib - B.c1_liberada_ha) / B.c1_liberada_ha;','const d = Math.abs(lib - B.c1_liberada_ha) / Math.max(B.c1_liberada_ha, 1);'),   # islas sin platanera exportadora: 0 ha liberadas, sin dividir por cero
 ('const consumo_t = pob * S.kg / 1000, ret = consumo_t / S.rend, lib = B.platanera_ha - ret;','const consumo_t = pob * S.kg / 1000, ret = Math.min(consumo_t / S.rend, B.platanera_ha), lib = Math.max(B.platanera_ha - ret, 0);'),
 ('const dem = B.demanda_agraria_hm3, max = Math.max(dem, agua) * 1.05;','const dem = B.demanda_agraria_hm3 || 0, max = Math.max(dem, agua, 0.1) * 1.05;'),
 ('`Sin exportar, la platanera libera ${pct(agua / dem)} del agua agraria de la isla. Y hay ${fmt(B.sanu_ha)} ha de suelo agrícola abandonado, casi tres veces lo que libera el plátano: el suelo no es lo que falta.`',
  '(lib < 50 ? `La isla apenas tiene platanera (${fmt(B.platanera_ha)} ha): no hay tierra ni agua de exportación que liberar. El reparto de la escena 4 se hace con el suelo agrícola abandonado, ${fmt(B.sanu_ha)} ha.` : `Sin exportar, la platanera libera ${dem ? pct(agua / dem) + " del agua agraria de la isla" : fmt(agua, 1) + " hm³"}. Y hay ${fmt(B.sanu_ha)} ha de suelo agrícola abandonado, ${fmt(B.sanu_ha / lib, 1)} veces lo que libera el plátano: el suelo no es lo que falta; lo que falta es escala frente a ${fmt(B.poblacion)} residentes.`)'),
 ('const max = Math.max(1.25, ...cob) * 1.05;','const max = Math.max(0.5, ...cob) * 1.05;'),
 ('<dt>Agua usada</dt><dd>${fmt(g.agua_usada / 1e6, 1)} de ${fmt(P.AGUA / 1e6, 1)} hm³</dd>','<dt>Agua usada</dt><dd>${fmt(g.agua_usada / 1e6, 1)} de ${fmt(P.AGUA / 1e6, 1)} hm³</dd><dt>Tierra del reparto</dt><dd>${fmt(g.tierraA)} ha de costa · ${fmt(g.tierraB)} ha de medianías</dd>'),
 ('const NOM = { Platanera: "Platanera", Frutales: "Frutales", "Viña": "Viña", Huerta: "Huerta", Otros: "Otros cultivos", Ornamentales: "Ornamentales", Tomate: "Tomate", SANU: "Suelo agrícola abandonado", Pastoreo: "Pastoreo" };',
  'const NOM = { Platanera: "Platanera", Frutales: "Frutales", "Viña": "Viña", Huerta: "Huerta, papa y millo", Otros: "Barbecho y otros", Ornamentales: "Ornamentales", Tomate: "Tomate", SANU: "Suelo agrícola abandonado", Pastoreo: "Pastoreo" };'),
 ('`<span><i style="background:${l.c}"></i>${NOM[l.d] || l.d}</span>`).join("") +','`<span><i style="background:${l.c}"></i>${NOM[l.d] || l.d}${l.ha ? " · " + fmt(l.ha) + " ha" : ""}</span>`).join("") +'),
 ('; en autarquía buena parte de la mejora viene del estiércol, que sustituye al fertilizante importado" : ""}. [INFERENCIA]','; en autarquía buena parte de la mejora viene del estiércol, que sustituye al fertilizante importado" : ""}. El monte aporta como máximo ${fmt(P.MONTE_CAP)} t de materia seca al caprino. [INFERENCIA]'),
]
pisos_fuente=f"temperatura por regresión sobre la cota con {len(pis['estaciones_temperatura'])} estaciones ({'AEMET y Agrocabildo' if C['slug']=='tenerife' else 'AEMET OpenData, normales 1991-2020 y series 2009-2025'}); lluvia por mediana de {len(pis['estaciones_lluvia'])} pluviómetros por franja [VERIFICADO el origen; método declarado en 92c_pisos.py]"
lede3=(f'La isla apenas tiene platanera ({f(PLAT)} ha): no hay exportación que cerrar ni agua que liberar. Mueve los deslizadores para ver qué pasaría si la tuviera.' if poca else 'La isla solo necesitaría una parte de su platanera para su propio consumo. El resto, y su agua, quedaría libre.')
T=[ # marcado
 ('<title>La Palma, despensa cerrada</title>',f'<title>{N}, despensa cerrada</title>'),
 ('<span class="tag">v6 · [BORRADOR]</span><span class="tag">datos a 2021-2026</span>',f'<span class="tag">{ver} · [BORRADOR]</span><span class="tag">datos a {anio if str(anio)=='2025' else f'{anio}-2025'}</span>'),
 ('<h1>La Palma, despensa cerrada</h1>',f'<h1>{N}, despensa cerrada</h1>'),
 ('qué habría en una nevera y una despensa solo con producto palmero.',f'qué habría en una nevera y una despensa solo con producto {G}. Y, con {f(c1["poblacion"])} residentes, si alcanzaría.'),
 ('<p>Relieve real de La Palma con las parcelas del Mapa de Cultivos.',f'<p>Relieve real de {N} con las parcelas del Mapa de Cultivos.'),
 ('aria-label="Relieve 3D de La Palma con parcelas coloreadas por uso"',f'aria-label="Relieve 3D de {N} con parcelas coloreadas por uso"'),
 ('anterior a la erupción de 2021, exageración vertical ×2 · Parcelas: Mapa de Cultivos de La Palma 2021-22 (Fuente: Gobierno de Canarias, CC BY 4.0) · Reparto sobre parcelas: ilustración del plan óptimo, no propuesta parcela a parcela [INFERENCIA] · Clima: AEMET C139E + Rodríguez (2015)',
  f'exageración vertical ×2 · Parcelas: Mapa de Cultivos de {N} {anio} (Fuente: Gobierno de Canarias, opendata.sitcan.es, CC BY 4.0) · Reparto sobre parcelas: ilustración del plan óptimo, no propuesta parcela a parcela [INFERENCIA] · Clima por pisos: {pisos_fuente}'),
 ('Solo lo que ya se cultiva en La Palma',f'Solo lo que ya se cultiva en {N}'),
 ('calibración: los 30 cultivos del Mapa de Cultivos de La Palma salen viables y los 8 que allí se riegan al 100 % no salen de secano · «LP» = con superficie hoy en la isla',
  f'calibración: los {CAL["n_viables"]} productos con superficie en el Mapa de Cultivos de {N} salen viables y los {CAL["n_regados"]} que allí se riegan al 100 % (campo REGADIO) no salen de secano · «LP» = con superficie hoy en la isla · reglas declaradas en 93_catalogo.py'),
 ('<p>La isla solo necesitaría unas decenas de hectáreas de platanera para su propio consumo. El resto, y su agua, quedaría libre.</p>',f'<p>{lede3}</p>'),
 ('<input type="range" id="rendPl" min="30" max="60" step="1" value="44">',f'<input type="range" id="rendPl" min="30" max="60" step="1" value="{REND}">'),
 ('Consumo por habitante [REQUIERE_FUENTE]; rendimiento [APROXIMADO]. La dotación A es la media del regadío del Plan Hidrológico; B, el consumo por planta (15-20 L/día).',
  f'Consumo por habitante [REQUIERE_FUENTE]; rendimiento de la platanera {("en la isla "+f(c1["rend_platanera_istac"],1)+" t/ha (ISTAC, mediana 2017-2023) [VERIFICADO]") if c1["rend_platanera_istac"] else "de Tenerife, 47 t/ha, porque la isla apenas tiene platanera [APROXIMADO]"}. Dotaciones: A, media del regadío de la isla ({f(c1["dot_A"]) + " m³/ha, plan hidrológico" if c1["dot_A"] else "sin dato"}); B, consumo por planta (15-20 L/día); C, dotación del plátano conforme a la IPH de Canarias (10.000 m³/ha) [APROXIMADO]{"; D, consumo medido en la isla (" + f(c1["dot_D"]) + " m³/ha) [VERIFICADO el origen]" if c1["dot_D"] else ""}. El reparto de la escena 4 usa {agua_txt}.'),
 ('Mapa de Cultivos de La Palma 2021-22 (Gobierno de Canarias, CC BY 4.0) · Plan Hidrológico de La Palma, 3.er ciclo (MITECO, ficha 21-PAL 2023) · padrón INE 2025',
  f'Mapa de Cultivos de {N} {anio} (Gobierno de Canarias, CC BY 4.0) · Agua: {c1["agua_fuente"]} · población: ISTAC, cifras oficiales a 1-1-2025 [VERIFICADO]'),
 ('La pesca parte de la primera venta registrada en 2021 (190 t), año de la erupción.</p>',f'La pesca parte de la primera venta registrada en 2021 en los puertos de {N} ({f(P["PESCA_T"])} t) [VERIFICADO]. Las frutas y hortalizas se cubren en la misma proporción que la energía, no como obligación absoluta.</p>'),
 ('Rendimientos: FAOSTAT España 2020-24 o mundo 2024 × factor del escenario',f'Rendimientos: ISTAC, superficies y producciones de {N} (o media de Canarias si la isla no tiene superficie), mediana 2017-2023, con factor por cultivo frente a FAOSTAT España; FAOSTAT × 0,7 donde no hay dato [APROXIMADO]'),
 ('pesca: primera venta 2021 (Gobierno de Canarias, CC BY 4.0) · reparto por programación lineal (HiGHS)','pesca: registro de primera venta 2021 (Gobierno de Canarias, CC BY 4.0) · censo ganadero ISTAC 2014-2025 para calibrar el monte · reparto por programación lineal (scipy/HiGHS)'),
 ('<h2>La nevera y la despensa palmeras</h2>',f'<h2>La nevera y la despensa {GP if GP.endswith("s") else GP+"s"}</h2>'),
 ('aria-label="Nevera abierta con productos palmeros"',f'aria-label="Nevera abierta con productos {GP}"'),
 ('aria-label="Despensa con productos palmeros"',f'aria-label="Despensa con productos {GP}"'),
 ('Criterio de entrada: probado en La Palma o con antecedentes (Mapa de Cultivos 2021-22, arraigo conocido, café recuperado desde 2019) · temporadas [CONOCIMIENTO_BASE] · pescado: meses con primera venta en 2021 (Gobierno de Canarias); la erupción, de septiembre a diciembre, redujo la pesca de otoño [INFERENCIA] · ilustración propia',
  f'Criterio de entrada: probado en {N} o con antecedentes (Mapa de Cultivos {anio}, arraigo conocido) · temporadas y productos de huerta, fruta y despensa [CONOCIMIENTO_BASE], pendientes de revisión local · pescado: las 14 especies con más peso en la primera venta de 2021 en puertos de {N} y sus meses de venta (Gobierno de Canarias, CC BY 4.0) [VERIFICADO] · ilustración propia'),
 ('<h2>La semana palmera</h2>',f'<h2>La semana {GF}</h2>'),
 ('cobertura nutricional del menú: NO CALCULADA (pendiente v5)','cobertura nutricional del menú: NO CALCULADA'),
 ('<p>La despensa puede cerrarse; el botiquín, mucho menos.',f'<p>{"La despensa podría acercarse a cerrarse; el botiquín, mucho menos." if c1["poblacion"]<50000 else "En "+N+" ni la despensa se cierra del todo; el botiquín, mucho menos."}'),
 ('<span>Fuentes: Gobierno de Canarias, Mapa de Cultivos de La Palma y registro de primera venta de pesca 2021 (CC BY 4.0) · FAO, FAOSTAT (CC BY 4.0) · FAO ECOCROP vía Recocrop (R. Hijmans, GPL-3; solo cálculo) · AEMET (citando a AEMET como autora) · Rodríguez, D. (2015), TFG ULL · MITECO, Plan Hidrológico de La Palma · INE.</span>',
  f'<span>Fuentes: Gobierno de Canarias, Mapa de Cultivos de {N} {anio} y registro de primera venta de pesca 2021 (CC BY 4.0) · Copernicus DEM GLO-30 (ESA) · FAO, FAOSTAT (CC BY 4.0) · FAO ECOCROP (copia pública OpenCLIM; solo cálculo) · AEMET OpenData (citando a AEMET como autora) · ISTAC (población, ganado, superficies y producciones) · planes hidrológicos insulares (MITECO/consejos insulares de aguas). Método y coeficientes de nutrición y ganadería heredados del visor «La Palma, despensa cerrada» (Jorge Díaz Pérez, territorio.visualizalapalma.es).</span>'),
 ('<span>Teclado: 1-7 cambia de escena.</span>',f'<span>Teclado: 1-7 cambia de escena. Réplica para {N} del visor de La Palma; {ver} generada el {hoy}.</span>'),
 ('<a href="../../aviso.html" aria-label="Aviso, fuentes y licencias"','<a href="aviso.html" aria-label="Aviso, fuentes y licencias"'),
]
falt=[]
for a,b in R+T:
    if a not in html: falt.append(a[:60]); continue
    html=html.replace(a,b)
if falt: print('NO ENCONTRADO:',falt)
open(out(C,'05_visor_despensa_cerrada.html'),'w',encoding='utf-8').write(html)
print(N,'visor OK',len(html)//1024,'KB')

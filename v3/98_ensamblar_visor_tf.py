# -*- coding: utf-8 -*-
"""Ensambla el visor autocontenido 'Tenerife, despensa cerrada' a partir de la plantilla de La Palma (misma estructura,
mismo three.js incrustado) y de las salidas 95/97/94/04b. Un solo HTML sin red."""
import os
REF=os.environ.get('DESPENSA_REF',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','_ref'))
import json, re, datetime
src=open(os.path.join(REF,'lapalma_visor.html'),encoding='utf-8').read()
cat=json.load(open('95_catalogo_salida_tf.json')); bal=json.load(open('97_balance_salida_tf.json')); terr=json.load(open('94_territorio_salida_tf.json')); coc=json.load(open('04b_cocina_tf.json'))
CAL=cat['calibra']
D={'cat':cat['cat'],'clima':cat['clima'],'calibra':cat['calibra'],'c1':bal['c1'],'param':bal['param'],'cult':bal['cult'],'bases':bal['bases'],'rejilla':bal['rejilla'],
   'nevera':coc['nevera'],'menu':coc['menu'],'botiquin':coc['botiquin'],'terr':terr['terr'],'alt':terr['alt'],'texHoy':terr['texHoy'],'texFut':terr['texFut']}
# ---- sustituir el bloque de datos
i=src.find('const D = {'); j=src.find('\n',i)
assert i>0 and src[j-1]==';'
html=src[:i]+'const D = '+json.dumps(D,ensure_ascii=False,separators=(',',':'))+';'+src[j:]
# ---- lógica: cotas, vertientes, textos
R=[
 ('const COTAS = [[0, 300], [300, 600], [600, 1000], [1000, 1500], [1500, 2426]]','const COTAS = [[0, 300], [300, 600], [600, 1000], [1000, 1500], [1500, 3715]]'),
 ('for (const v of ["E", "O"])','for (const v of ["N", "S"])'),
 ('v === "E" ? " · " + c.nombre','v === "N" ? " · " + c.nombre'),
 ('<dt>Hoy en La Palma</dt>','<dt>Hoy en Tenerife</dt>'),
 ('alt="Mapa de La Palma con parcelas coloreadas"','alt="Mapa de Tenerife con parcelas coloreadas"'),
 ('"Hoy (Mapa de Cultivos 2021-22)"','"Hoy (Mapa de Cultivos 2020-21)"'),
 ('Escenario del reparto: insumos actuales, 30 % del suelo abandonado recuperado y ganadería. La platanera (${fmt(T.platanera_ha)} ha) se reparte entre cultivos por orden de exigencia de calor: lo más cálido, en las parcelas más bajas. Del suelo abandonado se recuperan las ${fmt(T.recuperada_ha)} ha de menor pendiente. [INFERENCIA]',
  'Escenario del reparto: insumos actuales, 30 % del suelo abandonado recuperado y ganadería. La platanera (${fmt(T.platanera_ha)} ha) se reparte entre cultivos y forraje por orden de exigencia de calor: lo más cálido, en las parcelas más bajas. Del suelo abandonado (${fmt(D.param.SANU)} ha) se recuperan las ${fmt(T.recuperada_ha)} ha de menor pendiente. ${fmt(T.parcelas)} parcelas. [INFERENCIA]'),
 ('(f.nombre).replace','(f.nombre).replace'),
 ('const reduce = window.matchMedia','const reduce = window.matchMedia'),
 ('objetivo = new THREE.Vector3(0, 0, 1.5)','objetivo = new THREE.Vector3(0, 0, 0.5)'),
 ('const V = { oblicua: [0.35, 0.9, 55], cenital: [0, 0.02, 62], sur: [Math.PI, 0.98, 55] };','const V = { oblicua: [0.35, 0.9, 92], cenital: [0, 0.02, 100], sur: [Math.PI, 0.98, 92] };'),
 ('rad = Math.min(95, Math.max(10, rad * d0 / d))','rad = Math.min(160, Math.max(15, rad * d0 / d))'),
 ('rad = Math.min(95, Math.max(10, rad * (e.deltaY > 0 ? 1.1 : 0.9)))','rad = Math.min(160, Math.max(15, rad * (e.deltaY > 0 ? 1.1 : 0.9)))'),
 ('const cam = new THREE.PerspectiveCamera(38, 1, 0.1, 500)','const cam = new THREE.PerspectiveCamera(38, 1, 0.1, 800)'),
 ('const d = Math.abs(lib - B.c1_liberada_ha) / B.c1_liberada_ha;','const d = Math.abs(lib - B.c1_liberada_ha) / B.c1_liberada_ha;'),
 # Escena 3: lectura
 ('`Sin exportar, la platanera libera ${pct(agua / dem)} del agua agraria de la isla. Y hay ${fmt(B.sanu_ha)} ha de suelo agrícola abandonado, casi tres veces lo que libera el plátano: el suelo no es lo que falta.`',
  '`Sin exportar, la platanera libera ${pct(agua / dem)} del agua agraria de la isla. Y hay ${fmt(B.sanu_ha)} ha de suelo agrícola abandonado, más de cinco veces lo que libera el plátano: el suelo no es lo que falta; lo que falta es escala frente a ${fmt(B.poblacion)} residentes.`'),
 # Escena 4: cobertura texto
 ('`<span class="eyebrow">Cobertura de ${fmt(P.POB)} residentes · gris: producción actual sin plátano · azul: pesca · color: el reparto · línea: 100 %</span>`','`<span class="eyebrow">Cobertura de ${fmt(P.POB)} residentes · gris: producción actual sin plátano · azul: pesca · color: el reparto · línea: 100 %</span>`'),
 ('const max = Math.max(1.25, ...cob) * 1.05;','const max = Math.max(0.5, ...cob) * 1.05;'),
 ('<dt>Agua usada</dt><dd>${fmt(g.agua_usada / 1e6, 1)} de ${fmt(P.AGUA / 1e6, 1)} hm³</dd>','<dt>Agua usada</dt><dd>${fmt(g.agua_usada / 1e6, 1)} de ${fmt(P.AGUA / 1e6, 1)} hm³</dd><dt>Tierra del reparto</dt><dd>${fmt(g.tierraA)} ha de costa · ${fmt(g.tierraB)} ha de medianías</dd>'),
 ('const NOM = { Platanera: "Platanera", Frutales: "Frutales", "Viña": "Viña", Huerta: "Huerta", Otros: "Otros cultivos", Ornamentales: "Ornamentales", Tomate: "Tomate", SANU: "Suelo agrícola abandonado", Pastoreo: "Pastoreo" };',
  'const NOM = { Platanera: "Platanera", Frutales: "Frutales", "Viña": "Viña", Huerta: "Huerta, papa y millo", Otros: "Barbecho y otros", Ornamentales: "Ornamentales", Tomate: "Tomate", SANU: "Suelo agrícola abandonado", Pastoreo: "Pastoreo" };'),
 ('`<span><i style="background:${l.c}"></i>${NOM[l.d] || l.d}</span>`).join("") +','`<span><i style="background:${l.c}"></i>${NOM[l.d] || l.d}${l.ha ? " · " + fmt(l.ha) + " ha" : ""}</span>`).join("") +'),
 # Escena 5 ficha
 ('Temporada: ${it.m.length === 12 ? "todo el año"','Temporada: ${it.m.length === 12 ? "todo el año"'),
 # Reparto nota
 ('; en autarquía buena parte de la mejora viene del estiércol, que sustituye al fertilizante importado" : ""}. [INFERENCIA]','; en autarquía buena parte de la mejora viene del estiércol, que sustituye al fertilizante importado" : ""}. El monte aporta como máximo ${fmt(P.MONTE_CAP)} t de materia seca al caprino. [INFERENCIA]'),
]
for a,b in R:
    if a not in html: print('NO ENCONTRADO:',a[:70]); continue
    html=html.replace(a,b)
# ---- marcado
T=[
 ('<title>La Palma, despensa cerrada</title>','<title>Tenerife, despensa cerrada</title>'),
 ('<span class="tag">v6 · [BORRADOR]</span><span class="tag">datos a 2021-2026</span>','<span class="tag">v3 · [BORRADOR]</span><span class="tag">datos a 2021-2025</span>'),
 ('<h1>La Palma, despensa cerrada</h1>','<h1>Tenerife, despensa cerrada</h1>'),
 ('qué habría en una nevera y una despensa solo con producto palmero.','qué habría en una nevera y una despensa solo con producto tinerfeño. Y, con casi un millón de residentes, si alcanzaría.'),
 ('<p>Relieve real de La Palma con las parcelas del Mapa de Cultivos.','<p>Relieve real de Tenerife con las parcelas del Mapa de Cultivos.'),
 ('aria-label="Relieve 3D de La Palma con parcelas coloreadas por uso"','aria-label="Relieve 3D de Tenerife con parcelas coloreadas por uso"'),
 ('anterior a la erupción de 2021, exageración vertical ×2 · Parcelas: Mapa de Cultivos de La Palma 2021-22 (Fuente: Gobierno de Canarias, CC BY 4.0) · Reparto sobre parcelas: ilustración del plan óptimo, no propuesta parcela a parcela [INFERENCIA] · Clima: AEMET C139E + Rodríguez (2015)',
  'exageración vertical ×2 · Parcelas: Mapa de Cultivos de Tenerife 2021 (Fuente: Gobierno de Canarias, opendata.sitcan.es, CC BY 4.0) · Reparto sobre parcelas: ilustración del plan óptimo, no propuesta parcela a parcela [INFERENCIA] · Clima por pisos: temperatura por regresión sobre la cota con 16 estaciones de AEMET (normales 1991-2020 y series 2009-2025) y 40 de Agrocabildo (2001-2007); lluvia por mediana de los pluviómetros de cada franja, 224 de Agrocabildo (1983-2010) más AEMET [VERIFICADO]; detalle en 92c_pisos_climaticos_tf.py'),
 ('Solo lo que ya se cultiva en La Palma','Solo lo que ya se cultiva en Tenerife'),
 ('calibración: los 30 cultivos del Mapa de Cultivos de La Palma salen viables y los 8 que allí se riegan al 100 % no salen de secano · «LP» = con superficie hoy en la isla',
  f'calibración: los {CAL["n_viables"]} productos con superficie en el Mapa de Cultivos de Tenerife salen viables y los {CAL["n_regados"]} que allí se riegan al 100 % (campo REGADIO) no salen de secano · «LP» = con superficie hoy en la isla · reglas declaradas en 93_catalogo_viabilidad_tf.py'),
 ('<p>La isla solo necesitaría unas decenas de hectáreas de platanera para su propio consumo. El resto, y su agua, quedaría libre.</p>','<p>La isla solo necesitaría unos cientos de hectáreas de platanera para su propio consumo. El resto, y su agua, quedaría libre.</p>'),
 ('La dotación A es la media del regadío del Plan Hidrológico; B, el consumo por planta (15-20 L/día).','La dotación A es la media del regadío de la isla según la memoria del Plan Hidrológico de Tenerife (84,23 hm³ consumidos en regadío en 2016 entre 12.304 ha regadas en 2021); B, el consumo por planta (15-20 L/día).'),
 ('Mapa de Cultivos de La Palma 2021-22 (Gobierno de Canarias, CC BY 4.0) · Plan Hidrológico de La Palma, 3.er ciclo (MITECO, ficha 21-PAL 2023) · padrón INE 2025','Mapa de Cultivos de Tenerife 2021 (Gobierno de Canarias, CC BY 4.0): platanera 100 % regada, 1.448 ha bajo invernadero · Plan Hidrológico de Tenerife, 3.er ciclo, memoria (Consejo Insular de Aguas, 2023) [VERIFICADO] · población: ISTAC, cifras oficiales a 1-1-2025 [VERIFICADO]'),
 ('La pesca parte de la primera venta registrada en 2021 (190 t), año de la erupción.</p>','La pesca parte de la primera venta registrada en 2021 en los puertos de Tenerife (4.279 t, de ellas 2.680 de túnidos) [VERIFICADO]. Las frutas y hortalizas se cubren en la misma proporción que la energía, no como obligación absoluta.</p>'),
 ('pesca: primera venta 2021 (Gobierno de Canarias, CC BY 4.0) · reparto por programación lineal (HiGHS)','pesca: registro de primera venta 2021 (Gobierno de Canarias, CC BY 4.0) · censo ganadero ISTAC 2025 para calibrar el monte · reparto por programación lineal (scipy/HiGHS)'),
 ('<h2>La nevera y la despensa palmeras</h2>','<h2>La nevera y la despensa tinerfeñas</h2>'),
 ('aria-label="Nevera abierta con productos palmeros"','aria-label="Nevera abierta con productos tinerfeños"'),
 ('aria-label="Despensa con productos palmeros"','aria-label="Despensa con productos tinerfeños"'),
 ('Criterio de entrada: probado en La Palma o con antecedentes (Mapa de Cultivos 2021-22, arraigo conocido, café recuperado desde 2019) · temporadas [CONOCIMIENTO_BASE] · pescado: meses con primera venta en 2021 (Gobierno de Canarias); la erupción, de septiembre a diciembre, redujo la pesca de otoño [INFERENCIA] · ilustración propia',
  'Criterio de entrada: probado en Tenerife o con antecedentes (Mapa de Cultivos 2021, arraigo conocido) · temporadas de huerta y fruta [CONOCIMIENTO_BASE] · pescado: las 14 especies con más peso en la primera venta de 2021 en puertos de Tenerife y sus meses de venta (Gobierno de Canarias, CC BY 4.0) [VERIFICADO] · ilustración propia'),
 ('<h2>La semana palmera</h2>','<h2>La semana tinerfeña</h2>'),
 ('cobertura nutricional del menú: NO CALCULADA (pendiente v5)','cobertura nutricional del menú: NO CALCULADA (pendiente v4)'),
 ('<p>La despensa puede cerrarse; el botiquín, mucho menos.','<p>En Tenerife ni la despensa se cierra del todo; el botiquín, mucho menos.'),
 ('<span>Fuentes: Gobierno de Canarias, Mapa de Cultivos de La Palma y registro de primera venta de pesca 2021 (CC BY 4.0) · FAO, FAOSTAT (CC BY 4.0) · FAO ECOCROP vía Recocrop (R. Hijmans, GPL-3; solo cálculo) · AEMET (citando a AEMET como autora) · Rodríguez, D. (2015), TFG ULL · MITECO, Plan Hidrológico de La Palma · INE.</span>',
  '<span>Fuentes: Gobierno de Canarias, Mapa de Cultivos de Tenerife 2021 y registro de primera venta de pesca 2021 (CC BY 4.0) · Copernicus DEM GLO-30 (ESA) · FAO, FAOSTAT (CC BY 4.0) · FAO ECOCROP (copia pública OpenCLIM; solo cálculo) · AEMET OpenData, normales 1991-2020 y series 2009-2025 (citando a AEMET como autora) · Cabildo de Tenerife, Agrocabildo (temperatura 2001-2007 y transectos pluviométricos 1983-2010) · Consejo Insular de Aguas de Tenerife, memoria del Plan Hidrológico 3.er ciclo · ISTAC, cifras oficiales de población 2025 y efectivos de ganado 2014-2025. Método y coeficientes de rendimiento, nutrición y ganadería heredados del visor «La Palma, despensa cerrada» (Jorge Díaz Pérez, territorio.visualizalapalma.es).</span>'),
 ('<span>Teclado: 1-7 cambia de escena.</span>','<span>Teclado: 1-7 cambia de escena. Réplica para Tenerife del visor de La Palma; v3 generada el '+datetime.date.today().strftime('%d/%m/%Y')+'.</span>'),
 ('<a href="../../aviso.html" aria-label="Aviso, fuentes y licencias"','<a href="aviso_tf.html" aria-label="Aviso, fuentes y licencias"'),
]
for a,b in T:
    if a not in html: print('NO ENCONTRADO (markup):',a[:70]); continue
    html=html.replace(a,b)
open('05_visor_despensa_cerrada_tf_v3.html','w',encoding='utf-8').write(html)
print('OK',len(html)//1024,'KB')

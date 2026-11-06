# 04 · Lectura del balance de suficiencia de Tenerife (v4) [BORRADOR]

Corte: 06/11/2026. Método y coeficientes de nutrición y ganadería heredados del visor «La Palma, despensa cerrada» v6; tierra, agua, población, pesca, censo, clima y rendimientos agrícolas de fuentes directas de Tenerife.

## Cifras de partida (C1–C2)

- Residentes: 961.745 (ISTAC, cifras oficiales a 1-1-2025) [VERIFICADO]
- Platanera: 3.935,1 ha, el 100 % con riego y 1.448 ha bajo invernadero (Mapa de Cultivos de Tenerife 2021) [VERIFICADO]; retenida para consumo local a 15 kg/hab·año [REQUIERE_FUENTE] y 46,6 t/ha (ISTAC, mediana 2017-2023) [VERIFICADO]: 306,9 ha; liberada: 3.628,1 ha
- Agua liberada: 44,9 hm³/año con la dotación medida de la platanera en Tenerife (D: 12.375 m³/ha, Estudio de Consumos Hídricos del Cabildo, 2005, citado por C. Méndez) [VERIFICADO el origen]; alternativas: A media del regadío 6.846 m³/ha (24,8 hm³), B por planta 31,8–42,4 hm³, C IPH de Canarias 10.000 m³/ha (36,3 hm³). La D equivale al 53 % del consumo en regadío de la isla, coherente con el 60 % que la fuente atribuye al plátano.
- Suelo agrícola no utilizado: 19.215,9 ha (15.966 de abandono prolongado y 3.250 reciente; 971 con riego); barbecho: 2.382,2 ha (no entra en v2) [VERIFICADO]
- Pesca: 4.278,7 t vendidas en primera venta en puertos de Tenerife en 2021, de ellas 3.025 de túnidos; Canarias 8.592 t [VERIFICADO]
- Censo ganadero 2025 (ISTAC): 28.452 cabras, 5.137 bovinos, 6.797 ovejas, 20.400 cerdos, 1.812.705 gallinas [VERIFICADO]
- Necesidades: 2.250 kcal, 55 g de proteína, 70 g de grasa y 400 g de frutas y hortalizas por persona y día [APROXIMADO]

## Pisos climáticos (v3: estaciones reales)

| Piso | Cota | T media | T mes frío | Mín. abs. media | Lluvia | Pluviómetros | H. frío |
|---|---|---:|---:|---:|---:|---:|---:|
| P1-N · Costa | 0-300 m | 19,3 °C | 16,7 °C | 11,3 °C | 323 mm | 31 | 2 |
| P2-N · Medianías bajas | 300-600 m | 16,9 °C | 14,5 °C | 8,7 °C | 505 mm | 38 | 25 |
| P3-N · Medianías altas | 600-1000 m | 14,2 °C | 11,8 °C | 5,7 °C | 606 mm | 30 | 203 |
| P4-N · Pinar y cumbre baja | 1000-1500 m | 10,7 °C | 8,4 °C | 1,8 °C | 701 mm | 20 | 1385 |
| P5-N · Cumbre | 1500-3715 m | 10,6 °C | 6,3 °C | -1,6 °C | 481 mm | 11 | 2797 |
| P1-S · Costa | 0-300 m | 20,3 °C | 17,3 °C | 11,5 °C | 173 mm | 33 | 0 |
| P2-S · Medianías bajas | 300-600 m | 18,2 °C | 15,4 °C | 9,5 °C | 243 mm | 22 | 7 |
| P3-S · Medianías altas | 600-1000 m | 15,7 °C | 13,2 °C | 7,2 °C | 307 mm | 23 | 75 |
| P4-S · Pinar y cumbre baja | 1000-1500 m | 12,4 °C | 10,5 °C | 4,2 °C | 398 mm | 11 | 478 |
| P5-S · Cumbre | 1500-3715 m | 11,3 °C | 7,1 °C | -0,6 °C | 394 mm | 19 | 2259 |

Temperatura: regresión lineal sobre la cota por vertiente con las estaciones por debajo de 1.300 m (norte: 27 estaciones, -0.78 °C/100 m; sur: 24 estaciones, -0.72 °C/100 m) e interpolación hacia Izaña por encima. Las series cortas 2009-2025 de AEMET se corrigen con el sesgo medido frente a las normales (0.4 °C). Lluvia: mediana de los pluviómetros de cada franja y vertiente (Agrocabildo 1983-2010 más AEMET). Vertiente norte = barlovento (norte y noreste); sur = sotavento (este, sur y oeste). [VERIFICADO el origen; método propio declarado en 92c]

## Rendimientos agrícolas (v4: ISTAC, superficies y producciones de Tenerife, mediana 2017-2023)

| Cultivo del modelo | FAOSTAT España (kg/ha) | ISTAC Tenerife 2017-2023 (kg/ha) | Factor |
|---|---:|---:|---:|
| Papa | 32.016 | 19.670 | 0.614 |
| Boniato | 12.603 | 11.219 | 0.89 |
| Millo (grano, gofio) | 12.090 | 2.061 | 0.17 |
| Judía seca | 898 | 836 | 0.931 |
| Ñame | 7.480 | — (×0,7) | 0.7 |
| Tomate | 81.009 | 71.959 | 0.888 |
| Col | 22.863 | 24.824 | 1.086 |
| Cebolla | 52.967 | 25.684 | 0.485 |
| Zanahoria | 56.126 | 30.000 | 0.535 |
| Calabaza y bubango | 46.204 | 42.057 | 0.91 |
| Lechuga | 28.417 | 21.121 | 0.743 |
| Plátano (consumo local) | 46.313 | 46.607 | 1.006 |
| Papaya | 31.326 | 68.638 | 2.191 |
| Mango | 9.818 | 16.398 | 1.67 |
| Caña de azúcar (miel de caña) | 72.000 | 46.273 | 0.643 |
| Cacahuete | 3.300 | — (×0,7) | 0.7 |
| Trigo (gofio) | 3.399 | 1.095 | 0.322 |
| Cebada (gofio) | 3.136 | 853 | 0.272 |
| Centeno | 2.256 | 696 | 0.309 |
| Garbanzo | 1.195 | 749 | 0.627 |
| Lenteja | 1.228 | 749 | 0.61 |
| Haba seca | 1.240 | 612 | 0.493 |
| Arveja seca | 1.327 | 583 | 0.44 |
| Chocho | 1.500 | 776 | 0.518 |
| Papa de secano | 16.008 | 19.670 | 0.614 |
| Castaña | 4.733 | 3.825 | 0.808 |
| Almendra | 453 | 501 | 1.106 |
| Higo | 3.100 | 4.151 | 1.339 |
| Olivo (aceite) | 2.562 | 3.869 | 1.51 |
| Girasol (aceite) | 1.100 | — (×0,7) | 0.7 |
| Papa (medianías, regadío) | 32.016 | 19.670 | 0.614 |
| Millo (medianías, regadío) | 12.090 | 2.061 | 0.17 |
| Hortalizas (medianías, regadío) | 40.000 | 32.570 | 0.814 |

Factor = rendimiento tinerfeño / referencia FAOSTAT España. Escenarios: insular = factor; autarquía = factor (abonado con estiércol) o factor × 5/7 (sin abono); España = máx(factor, 1). Sin dato ISTAC (cacahuete, girasol, ñame): FAOSTAT × 0,7 [APROXIMADO]. Fuente: ISTAC, conjuntos E01135A_000005 (producción recolectada) y E01135A_000003/000004 (superficie cultivada y de producción), Tenerife, mediana de los cocientes anuales 2017-2023 [VERIFICADO].

Producción actual (bases del balance), rendimientos usados:

| Producción actual | Referencia anterior (kg/ha) | ISTAC Tenerife (kg/ha) |
|---|---:|---:|
| Aguacate | 5.550 | 7.287 |
| Viña (uva) | 6.301 | 2.893 |
| Cítricos | 21.528 | 8.525 |
| Papa | 32.014 | 19.670 |
| Almendro | 460 | 501 |
| Mango | 9.818 | 16.398 |
| Hortalizas | 30.010 | 32.570 |
| Olivo (aceite) | 2.560 | 3.869 |
| Higuera | 3.068 | 4.151 |
| Boniato | 12.589 | 11.219 |
| Ñame | 7.496 | 5.248 |
| Millo | 12.063 | 2.061 |
| Plátano retenido | 46.307 | 46.607 |
| Cereal (trigo y cebada, gofio) | 3.399 | 1.095 |
| Papaya | 31.326 | 68.638 |
| Leguminosa seca | 898 | 836 |
| Frutales templados | 15.000 | 8.733 |
| Subtropicales (guayaba, chirimoya…) | 8.000 | 17.403 |
| Tunera | 8.000 | 2.968 |

## Cobertura mínima (energía, proteína, grasa y frutas y hortalizas) en los 132 escenarios

| Insumos | Ganado | Pesca | 0 % SANU | 30 % SANU | 100 % SANU |
|---|---|---|---:|---:|---:|
| Autarquía estricta | sin ganado | pesca 2021 | 8 % | 13 % | 24 % |
| Autarquía estricta | sin ganado | pesca ×3 | 8 % | 14 % | 25 % |
| Autarquía estricta | con ganado | pesca 2021 | 12 % | 20 % | 27 % |
| Autarquía estricta | con ganado | pesca ×3 | 13 % | 20 % | 28 % |
| Insular, insumos actuales | sin ganado | pesca 2021 | 10 % | 17 % | 32 % |
| Insular, insumos actuales | sin ganado | pesca ×3 | 10 % | 17 % | 33 % |
| Insular, insumos actuales | con ganado | pesca 2021 | 13 % | 22 % | 34 % |
| Insular, insumos actuales | con ganado | pesca ×3 | 14 % | 22 % | 35 % |
| Media de España | sin ganado | pesca 2021 | 14 % | 25 % | 52 % |
| Media de España | sin ganado | pesca ×3 | 14 % | 26 % | 53 % |
| Media de España | con ganado | pesca 2021 | 17 % | 28 % | 55 % |
| Media de España | con ganado | pesca ×3 | 17 % | 29 % | 56 % |

Lectura: **ningún escenario pasa del 56 %**. En el de referencia (insumos actuales, 30 % del suelo abandonado recuperado, ganado, pesca de 2021) la cobertura es del 22 %: energía 22 %, proteína 28 %, grasa 22 %, frutas y hortalizas 130 %. La producción actual sin plátano aporta el 11,0 % de la energía y la pesca el 2,2 % de la proteína. [INFERENCIA]

## Reparto del escenario de referencia (insular|0.3|1|1)

| Destino | Dónde | ha / cabezas | Producción | Factor |
|---|---|---:|---:|---:|
| Olivo (aceite) | medianías, secano | 1.729 | 6.691 t | 1.51 |
| Cacahuete | costa, regadío (ex platanera) | 1.088 | 2.514 t | 0.7 |
| Plátano (consumo local) | costa, regadío (ex platanera) | 935 | 43.552 t | 1.006 |
| Girasol (aceite) | medianías, secano | 565 | 435 t | 0.7 |
| Forraje regado (medianías) | medianías, regadío | 3.470 | 41.640 t MS |  |
| Millo forrajero (costa) | costa, regadío (ex platanera) | 1.605 | 24.073 t MS |  |
| Cabra tinerfeña | establo y monte | 37.143 | 14.857 t leche · 297 t carne |  |
| Vaca de leche | establo y monte | 8.110 | 36.494 t leche · 487 t carne |  |

Agua usada: 44,9 de 44,9 hm³. Tierra: 3.628 ha de costa y 5.765 ha de medianías de las 5.765 recuperables. El caprino está limitado por el monte (13.000 t MS/año).

## Pesca de Tenerife en 2021 (primera venta, 14 especies principales)

| Especie | t en 2021 |
|---|---:|
| Tuna | 1.663,7 |
| Barrilote | 670,0 |
| Caballa del Atlántico | 390,1 |
| Atún rojo o de aleta azul | 346,0 |
| Bonito o Bonito listado | 246,4 |
| Pez espada o Aguja paladar | 183,2 |
| Chicharro | 180,4 |
| Rabil | 99,1 |
| Sardina arencada | 98,2 |
| Vieja | 43,7 |
| Camarón narval | 34,4 |
| Pargo macho | 21,2 |
| Bocinegro | 19,6 |
| Fula colorada | 19,1 |

## La Palma frente a Tenerife

| | La Palma (v6) | Tenerife (v2) |
|---|---:|---:|
| Residentes | 86.194 | 961.745 |
| Platanera (ha) | 2.675 | 3.935 |
| Platanera retenida para consumo local (ha) | 29 | 328 |
| Tierra liberada (ha) | 2.646 | 3.607 |
| Agua liberada, dotación media (hm³/año) | 22,4 | 24,7 |
| Demanda agraria de la isla (hm³/año) | 41,1 | 84,23 |
| Suelo agrícola abandonado (ha) | 7.645 | 19.216 |
| Superficie agrícola del Mapa de Cultivos por cada 1.000 residentes (ha) | 162,0 | 40,3 |
| Pesca de partida, primera venta 2021 (t) | 190 | 4.279 |
| Cobertura mínima, insumos actuales, 30 % SANU, ganado | 110 % | 16 % |
| Cobertura mínima, mejor caso (España, 100 % SANU, pesca ×3) | 257 % | 38 % |

La diferencia no está en el clima ni en la nevera: está en la escala. Tenerife tiene once veces más residentes y solo 1,5 veces más platanera. [INFERENCIA]

## Cambios v3 → v4

- Rendimientos agrícolas medidos en Tenerife (ISTAC) para 30 cultivos del modelo, con factor por cultivo en vez del 0,7 uniforme: la papa rinde 0,61 de la referencia, el millo en grano 0,17, la cebolla 0,49, la zanahoria 0,53; la papaya 2,19, el mango 1,67, el olivo 1,51, el plátano 1,01.
- Agua liberada por el plátano: de la media del regadío (6.846 m³/ha, 24,8 hm³) a la dotación medida de la platanera (12.375 m³/ha, 44,9 hm³). El visor ofrece las cuatro dotaciones.
- Rendimiento de la platanera 44 → 46,6 t/ha (ISTAC): la isla retiene 307 ha en vez de 326.
- **Error corregido**: en las v1-v3 la producción actual de aguacate, viña, cítricos, papa, almendro, mango, hortalizas, olivo, higuera, batata, ñame, millo y plátano retenido se calculaba con el rendimiento en t/ha donde el modelo esperaba kg/ha, y salía mil veces menor. La «producción actual sin plátano» pasa del 1,1 % al 11,0 % de la energía.
- Cobertura de referencia 16 % → 22 %; mejor caso 38 % → 56 %. Con el agua del plátano medida, el reparto mete forraje regado en medianías y más plátano de consumo local.

## Cambios v2 → v3

| Piso | Lluvia v2 (interpolación) | Lluvia v3 (mediana de pluviómetros) | T media v2 | T media v3 |
|---|---:|---:|---:|---:|
| P1-N | 347 mm | 323 mm | 20,4 | 19,3 |
| P2-N | 463 mm | 505 mm | 17,4 | 16,9 |
| P3-N | 498 mm | 606 mm | 16,3 | 14,2 |
| P4-N | 451 mm | 701 mm | 14,6 | 10,7 |
| P5-N | 382 mm | 481 mm | 12,2 | 10,6 |
| P1-S | 131 mm | 173 mm | 21,0 | 20,3 |
| P2-S | 179 mm | 243 mm | 19,5 | 18,2 |
| P3-S | 234 mm | 307 mm | 17,6 | 15,7 |
| P4-S | 306 mm | 398 mm | 15,3 | 12,4 |
| P5-S | 331 mm | 394 mm | 12,4 | 11,3 |

- El mar de nubes ya cuenta: la lluvia de las medianías altas del norte sube de 498 a 606 mm y la del pinar de 451 a 701 mm; en el sur también sube en todas las franjas (costa 131 → 173 mm, medianías altas 234 → 307 mm), porque la interpolación de la v2 entre dos estaciones costeras muy secas infravaloraba el resto.
- Productos alimentarios de secano: 30 en la v2 → 50 en la v3 (90 con riego).
- Calibración con el campo REGADIO: 106/106.
- El balance no cambia (misma tierra, agua, población y pesca): cobertura de referencia 16 %, mejor caso 38 %.

## Cambios v1 → v2

- Población 955.063 → 961.745 (la cifra provisional era la de 2024).
- Dotación media 7.080 → 6.846 m³/ha (consumo 84,23 hm³ en 2016 y 12.304 ha regadas en 2021, leídos de la memoria del PHT).
- Pesca 3.500 → 4.278,7 t (registro de primera venta 2021).
- Techo del monte 20.000 → 13.000 t MS/año (censo ISTAC).
- Clima: de normales resumidas de memoria a interpolación entre siete estaciones; la lluvia de las medianías altas del norte baja (sin estación en el mar de nubes) y el catálogo pasa de 72 a 35 productos de secano.
- Calibración del catálogo con el campo REGADIO oficial: 106/106.
- Cobertura de referencia 17 % → 16 %; mejor caso 39 % → 38 %.

## Decisiones de la v4 (revisables)

1. Frutas y hortalizas como cuarta cobertura en proporción.
2. Techo del monte para el caprino: 13.000 t de materia seca al año.
3. Coeficientes de leche y carne de la cabra palmera aplicados a la cabra tinerfeña.
4. Ni el barbecho ni el suelo abandonado con riego entran aparte en la bolsa recuperable.
5. Pisos climáticos: dos vertientes, regresión de temperatura por debajo de 1.300 m, mediana de pluviómetros por franja.
6. Rendimientos: factor por cultivo ISTAC/FAOSTAT; España = máx(factor, 1); sin dato, 0,7.
7. Agua del plátano: dotación D (12.375 m³/ha, Cabildo 2005) por defecto.

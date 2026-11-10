# 04 · Lectura del balance de suficiencia de El Hierro (v1) [BORRADOR]

Corte: 10/11/2026. Pipeline multi-isla; método y coeficientes de nutrición y ganadería heredados del visor «La Palma, despensa cerrada» v6 y del de Tenerife v4.

## Cifras de partida (C1–C2)

- Residentes: 12.040 (ISTAC, cifras oficiales a 1-1-2025) [VERIFICADO]
- Platanera: 59,9 ha (58 ha bajo invernadero) en el Mapa de Cultivos de El Hierro 2022 [VERIFICADO]; retenida para consumo local a 15 kg/hab·año [REQUIERE_FUENTE] y 47,3 t/ha: 3,8 ha; liberada: 56,1 ha
- Agua liberada: 0,6 hm³/año con la dotación C (10.000 m³/ha), el 33 % de la demanda agraria de la isla (1,72 hm³). Fuente del agua: Apéndice 1.23 MITECO (PH El Hierro 3.er ciclo): demanda agraria 1,72 hm³/año, 406 ha regadas [APROXIMADO]; dotación del plátano IPH 10.000 m³/ha
- Suelo agrícola no utilizado: 2.764,6 ha; barbecho: 59,1 ha (no entra) [VERIFICADO]
- Pesca: 133,7 t vendidas en primera venta en puertos de El Hierro en 2021 [VERIFICADO]
- Censo ganadero 2025 (ISTAC): 4910 caprino, 704 bovino, 2431 ovino, 496 porcino, 778 gallinas; techo del monte 2.500 t MS/año [APROXIMADO]
- Necesidades: 2.250 kcal, 55 g de proteína, 70 g de grasa y 400 g de frutas y hortalizas por persona y día [APROXIMADO]

## Pisos climáticos

| Piso | Cota | T media | T mes frío | Mín. abs. est. | Lluvia | Pluviómetros | H. frío |
|---|---|---:|---:|---:|---:|---:|---:|
| P1-N · Costa | 0-300 m | 20,6 °C | 17,0 °C | 11,0 °C | 130 mm | 0 (regresión log-lluvia/cota (regional anclada)) | 0 |
| P2-N · Medianías bajas | 300-600 m | 18,7 °C | 15,0 °C | 9,0 °C | 201 mm | 0 (regresión log-lluvia/cota (regional anclada)) | 9 |
| P3-N · Medianías altas | 600-1000 m | 16,4 °C | 12,8 °C | 6,7 °C | 334 mm | 0 (regresión log-lluvia/cota (regional anclada)) | 91 |
| P4-N · Cumbre | 1000-1501 m | 13,8 °C | 10,2 °C | 4,1 °C | 599 mm | 0 (regresión log-lluvia/cota (regional anclada)) | 542 |
| P1-S · Costa | 0-300 m | 20,6 °C | 17,0 °C | 11,0 °C | 130 mm | 0 (regresión log-lluvia/cota (regional anclada)) | 0 |
| P2-S · Medianías bajas | 300-600 m | 18,7 °C | 15,0 °C | 9,0 °C | 201 mm | 0 (regresión log-lluvia/cota (regional anclada)) | 9 |
| P3-S · Medianías altas | 600-1000 m | 16,4 °C | 12,8 °C | 6,7 °C | 334 mm | 1 (regresión log-lluvia/cota (regional anclada)) | 91 |
| P4-S · Cumbre | 1000-1501 m | 13,8 °C | 10,2 °C | 4,1 °C | 599 mm | 0 (regresión log-lluvia/cota (regional anclada)) | 542 |

Temperaturas por regresión sobre la cota con las estaciones de cada vertiente (barlovento N, sotavento S); lluvia por mediana de los pluviómetros de cada franja. vertiente N: menos de 3 estaciones de temperatura; regresión con todas las de la isla lluvia: solo 1 pluviómetro(s) en la isla; se aplica la pendiente regional de Canarias (60 estaciones AEMET ≤1500 m, +0.15 ln(mm)/100 m) anclada en los de la isla [APROXIMADO] vertiente S: menos de 3 estaciones de temperatura; regresión con todas las de la isla Estaciones: 2 de temperatura y 1 pluviómetros. Sesgo de las series cortas frente a las normales: 0.38 °C.

## Rendimientos agrícolas (ISTAC, mediana 2017-2023)

| Cultivo del modelo | Bolsa | FAOSTAT España (kg/ha) | ISTAC (kg/ha) | Factor | Fuente | Viabilidad en la isla (catálogo) |
|---|---|---:|---:|---:|---|---|
| Papa | A | 32.016 | 19.469 | 0.608 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Boniato | A | 12.603 | 12.000 | 0.952 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 416 mm) |
| Millo (grano, gofio) | A | 12.090 | 2.554 | 0.211 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 1 mm) |
| Judía seca | A | 898 | 829 | 0.923 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 166 mm) |
| Ñame | A | 7.480 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 1466 mm) |
| Tomate | A | 81.009 | 95.725 | 1.182 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 1 mm) |
| Col | A | 22.863 | 25.364 | 1.109 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Cebolla | A | 52.967 | 25.000 | 0.472 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 0 mm) |
| Zanahoria | A | 56.126 | 30.000 | 0.535 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Calabaza y bubango | A | 46.204 | 31.207 | 0.675 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 1 mm) |
| Lechuga | A | 28.417 | 27.871 | 0.981 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 501 mm) |
| Plátano (consumo local) | A | 46.313 | 47.073 | 1.016 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 2199 mm) |
| Papaya | A | 31.326 | 59.191 | 1.89 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 1166 mm) |
| Mango | A | 9.818 | 14.235 | 1.45 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 470 mm) |
| Caña de azúcar (miel de caña) | A | 72.000 | 44.430 | 0.617 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 1299 mm) |
| Cacahuete | A | 3.300 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 266 mm) |
| Trigo (gofio) | Bs | 3.399 | 967 | 0.285 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 151 mm) · **excluido** |
| Cebada (gofio) | Bs | 3.136 | 922 | 0.294 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Centeno | Bs | 2.256 | 878 | 0.389 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE SECANO |
| Garbanzo | Bs | 1.195 | 641 | 0.537 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Lenteja | Bs | 1.228 | 641 | 0.522 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Haba seca | Bs | 1.240 | 773 | 0.624 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 51 mm) |
| Arveja seca | Bs | 1.327 | 687 | 0.518 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 201 mm) · **excluido** |
| Chocho | Bs | 1.500 | 778 | 0.519 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 0 mm) |
| Papa de secano | Bs | 16.008 | 19.469 | 0.608 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Castaña | Bs | 4.733 | 5.033 | 1.063 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE SECANO |
| Almendra | Bs | 453 | 406 | 0.897 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Higo | Bs | 3.100 | 567 | 0.183 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Olivo (aceite) | Bs | 2.562 | 2.785 | 1.087 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE SECANO |
| Girasol (aceite) | Bs | 1.100 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 1 mm) |
| Papa (medianías, regadío) | Br | 32.016 | 19.469 | 0.608 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Millo (medianías, regadío) | Br | 12.090 | 2.554 | 0.211 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 1 mm) |
| Hortalizas (medianías, regadío) | Br | 40.000 | 21.346 | 0.534 | ISTAC 2017-2023, isla | sin entrada en el catálogo (se admite) |

Cultivos del modelo excluidos por el catálogo de la isla (no viables en secano con la lluvia de sus pisos, o no viables): Trigo (gofio) (VIABLE CON RIEGO (déficit 151 mm)); Arveja seca (VIABLE CON RIEGO (déficit 201 mm)). [DECISIÓN v5]

## Cobertura mínima en los 132 escenarios

| Insumos | Ganado | Pesca | 0 % SANU | 30 % SANU | 100 % SANU |
|---|---|---|---:|---:|---:|
| Autarquía estricta | sin ganado | pesca 2021 | 18 % | 61 % | 136 % |
| Autarquía estricta | sin ganado | pesca ×3 | 19 % | 65 % | 139 % |
| Autarquía estricta | con ganado | pesca 2021 | 26 % | 70 % | 146 % |
| Autarquía estricta | con ganado | pesca ×3 | 27 % | 71 % | 150 % |
| Insular, insumos actuales | sin ganado | pesca 2021 | 23 % | 81 % | 176 % |
| Insular, insumos actuales | sin ganado | pesca ×3 | 24 % | 86 % | 181 % |
| Insular, insumos actuales | con ganado | pesca 2021 | 30 % | 85 % | 180 % |
| Insular, insumos actuales | con ganado | pesca ×3 | 32 % | 89 % | 184 % |
| Media de España | sin ganado | pesca 2021 | 31 % | 127 % | 292 % |
| Media de España | sin ganado | pesca ×3 | 33 % | 129 % | 295 % |
| Media de España | con ganado | pesca 2021 | 37 % | 130 % | 292 % |
| Media de España | con ganado | pesca ×3 | 38 % | 131 % | 295 % |

Lectura: **ningún escenario pasa del 295 %**. En el de referencia (insumos actuales, 30 % del suelo abandonado recuperado, ganado, pesca de 2021) la cobertura es del 85 %: energía 85 %, proteína 85 %, grasa 85 %, frutas y hortalizas 366 %. La producción actual sin plátano aporta el 33,7 % de la energía y la pesca el 5,5 % de la proteína. [INFERENCIA]

## Reparto del escenario de referencia (insular|0.3|1|1)

| Destino | Dónde | ha / cabezas | Producción | Factor |
|---|---|---:|---:|---:|
| Castaña | medianías, secano | 249 | 1.252 t | 1.063 |
| Olivo (aceite) | medianías, secano | 249 | 693 t | 1.087 |
| Chocho | medianías, secano | 136 | 106 t | 0.519 |
| Girasol (aceite) | medianías, secano | 89 | 69 t | 0.7 |
| Papa de secano | medianías, secano | 66 | 647 t | 0.608 |
| Tomate | costa, regadío (ex platanera) | 17 | 1.612 t | 1.182 |
| Cacahuete | costa, regadío (ex platanera) | 17 | 39 t | 0.7 |
| Forraje regado (medianías) | medianías, regadío | 40 | 478 t MS |  |
| Millo forrajero (costa) | costa, regadío (ex platanera) | 22 | 337 t MS |  |
| Cabra majorera (El Hierro) | establo y monte | 2.327 | 931 t leche · 19 t carne |  |

Agua usada: 0,6 de 0,6 hm³. Tierra: 56 ha de costa y 829 ha de medianías de las 829 recuperables.

## Decisiones (revisables)

1. Frutas y hortalizas como cuarta cobertura en proporción.
2. Techo del monte para el caprino: 0,35 t MS por cabra sobre el máximo del censo ISTAC 2014-2025.
3. Rendimientos: factor por cultivo ISTAC/FAOSTAT (isla, o media de Canarias si la isla no tiene superficie); España = máx(factor, 1); sin dato, 0,7.
4. Dotación del plátano: C por defecto.
5. Pisos climáticos: dos vertientes, regresión de temperatura, mediana de pluviómetros por franja (regresión del logaritmo de la lluvia sobre la cota donde faltan pluviómetros; pendiente regional de Canarias si la isla tiene menos de 3).
6. Viabilidad en el balance (v5): un cultivo de secano (Bs) solo entra si el catálogo lo da VIABLE SECANO o VIABLE CON RIEGO con déficit ≤150 mm; los de regadío (A, Br) si es VIABLE SECANO o VIABLE CON RIEGO. Forraje de secano: 3.0 t MS/ha (3 t/ha con ≥500 mm en el piso más lluvioso, proporcional por debajo).

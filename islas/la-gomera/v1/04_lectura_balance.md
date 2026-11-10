# 04 · Lectura del balance de suficiencia de La Gomera (v1) [BORRADOR]

Corte: 10/11/2026. Pipeline multi-isla; método y coeficientes de nutrición y ganadería heredados del visor «La Palma, despensa cerrada» v6 y del de Tenerife v4.

## Cifras de partida (C1–C2)

- Residentes: 22.442 (ISTAC, cifras oficiales a 1-1-2025) [VERIFICADO]
- Platanera: 133,1 ha (17 ha bajo invernadero) en el Mapa de Cultivos de La Gomera 2023 [VERIFICADO]; retenida para consumo local a 15 kg/hab·año [REQUIERE_FUENTE] y 32,0 t/ha: 10,5 ha; liberada: 122,6 ha
- Agua liberada: 1,2 hm³/año con la dotación C (10.000 m³/ha), el 23 % de la demanda agraria de la isla (5,34 hm³). Fuente del agua: Apéndice 1.22 MITECO (PH La Gomera 3.er ciclo): demanda agraria 5,34 hm³/año, 970 ha regadas [APROXIMADO]; dotación del plátano IPH 10.000 m³/ha
- Suelo agrícola no utilizado: 3.457,5 ha; barbecho: 109,8 ha (no entra) [VERIFICADO]
- Pesca: 229,4 t vendidas en primera venta en puertos de La Gomera en 2021 [VERIFICADO]
- Censo ganadero 2025 (ISTAC): 3031 caprino, 27 bovino, 177 ovino, 91 porcino, 3826 gallinas; techo del monte 2.200 t MS/año [APROXIMADO]
- Necesidades: 2.250 kcal, 55 g de proteína, 70 g de grasa y 400 g de frutas y hortalizas por persona y día [APROXIMADO]

## Pisos climáticos

| Piso | Cota | T media | T mes frío | Mín. abs. est. | Lluvia | Pluviómetros | H. frío |
|---|---|---:|---:|---:|---:|---:|---:|
| P1-N · Costa | 0-300 m | 18,9 °C | 16,1 °C | 9,6 °C | 172 mm | 1 (regresión log-lluvia/cota (isla)) | 4 |
| P2-N · Medianías bajas | 300-600 m | 17,8 °C | 14,6 °C | 8,4 °C | 223 mm | 0 (regresión log-lluvia/cota (isla)) | 21 |
| P3-N · Medianías altas | 600-1000 m | 16,6 °C | 12,9 °C | 7,1 °C | 304 mm | 2 (regresión log-lluvia/cota (isla)) | 87 |
| P4-N · Cumbre | 1000-1487 m | 15,1 °C | 10,9 °C | 5,6 °C | 432 mm | 0 (regresión log-lluvia/cota (isla)) | 394 |
| P1-S · Costa | 0-300 m | 20,9 °C | 18,0 °C | 12,1 °C | 119 mm | 3 (mediana de pluviómetros) | 0 |
| P2-S · Medianías bajas | 300-600 m | 19,1 °C | 16,2 °C | 8,9 °C | 178 mm | 0 (regresión log-lluvia/cota (vertiente)) | 4 |
| P3-S · Medianías altas | 600-1000 m | 17,0 °C | 14,1 °C | 5,2 °C | 245 mm | 0 (regresión log-lluvia/cota (vertiente)) | 40 |
| P4-S · Cumbre | 1000-1487 m | 14,6 °C | 11,7 °C | 1,0 °C | 353 mm | 1 (regresión log-lluvia/cota (vertiente)) | 224 |

Temperaturas por regresión sobre la cota con las estaciones de cada vertiente (barlovento N, sotavento S); lluvia por mediana de los pluviómetros de cada franja.  Estaciones: 7 de temperatura y 7 pluviómetros. Sesgo de las series cortas frente a las normales: 0.38 °C.

## Rendimientos agrícolas (ISTAC, mediana 2017-2023)

| Cultivo del modelo | Bolsa | FAOSTAT España (kg/ha) | ISTAC (kg/ha) | Factor | Fuente | Viabilidad en la isla (catálogo) |
|---|---|---:|---:|---:|---|---|
| Papa | A | 32.016 | 19.811 | 0.619 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 68 mm) |
| Boniato | A | 12.603 | 10.865 | 0.862 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 318 mm) |
| Millo (grano, gofio) | A | 12.090 | 2.815 | 0.233 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 168 mm) |
| Judía seca | A | 898 | 981 | 1.093 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 68 mm) |
| Ñame | A | 7.480 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 1496 mm) |
| Tomate | A | 81.009 | 45.304 | 0.559 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 168 mm) |
| Col | A | 22.863 | 24.561 | 1.074 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 68 mm) |
| Cebolla | A | 52.967 | 24.912 | 0.47 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 0 mm) |
| Zanahoria | A | 56.126 | 30.000 | 0.535 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 168 mm) |
| Calabaza y bubango | A | 46.204 | 29.954 | 0.648 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 168 mm) |
| Lechuga | A | 28.417 | 20.183 | 0.71 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 668 mm) |
| Plátano (consumo local) | A | 46.313 | 31.705 | 0.685 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 2222 mm) |
| Papaya | A | 31.326 | 59.513 | 1.9 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 1196 mm) |
| Mango | A | 9.818 | 17.741 | 1.807 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 481 mm) |
| Caña de azúcar (miel de caña) | A | 72.000 | 44.430 | 0.617 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 1068 mm) |
| Cacahuete | A | 3.300 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 168 mm) |
| Trigo (gofio) | Bs | 3.399 | 1.134 | 0.334 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 318 mm) · **excluido** |
| Cebada (gofio) | Bs | 3.136 | 1.258 | 0.401 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 68 mm) |
| Centeno | Bs | 2.256 | 878 | 0.389 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 168 mm) · **excluido** |
| Garbanzo | Bs | 1.195 | 953 | 0.797 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 168 mm) · **excluido** |
| Lenteja | Bs | 1.228 | 953 | 0.776 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 168 mm) · **excluido** |
| Haba seca | Bs | 1.240 | 773 | 0.624 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 218 mm) · **excluido** |
| Arveja seca | Bs | 1.327 | 687 | 0.518 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 368 mm) · **excluido** |
| Chocho | Bs | 1.500 | 778 | 0.519 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 0 mm) |
| Papa de secano | Bs | 16.008 | 19.811 | 0.619 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 68 mm) |
| Castaña | Bs | 4.733 | 5.033 | 1.063 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 468 mm) · **excluido** |
| Almendra | Bs | 453 | 1.084 | 2.392 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE SECANO |
| Higo | Bs | 3.100 | 1.957 | 0.631 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE SECANO |
| Olivo (aceite) | Bs | 2.562 | 2.785 | 1.087 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE SECANO |
| Girasol (aceite) | Bs | 1.100 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 168 mm) · **excluido** |
| Papa (medianías, regadío) | Br | 32.016 | 19.811 | 0.619 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 68 mm) |
| Millo (medianías, regadío) | Br | 12.090 | 2.815 | 0.233 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 168 mm) |
| Hortalizas (medianías, regadío) | Br | 40.000 | 22.198 | 0.555 | ISTAC 2017-2023, isla | sin entrada en el catálogo (se admite) |

Cultivos del modelo excluidos por el catálogo de la isla (no viables en secano con la lluvia de sus pisos, o no viables): Trigo (gofio) (VIABLE CON RIEGO (déficit 318 mm)); Centeno (VIABLE CON RIEGO (déficit 168 mm)); Garbanzo (VIABLE CON RIEGO (déficit 168 mm)); Lenteja (VIABLE CON RIEGO (déficit 168 mm)); Haba seca (VIABLE CON RIEGO (déficit 218 mm)); Arveja seca (VIABLE CON RIEGO (déficit 368 mm)); Castaña (VIABLE CON RIEGO (déficit 468 mm)); Girasol (aceite) (VIABLE CON RIEGO (déficit 168 mm)). [DECISIÓN v5]

## Cobertura mínima en los 132 escenarios

| Insumos | Ganado | Pesca | 0 % SANU | 30 % SANU | 100 % SANU |
|---|---|---|---:|---:|---:|
| Autarquía estricta | sin ganado | pesca 2021 | 12 % | 36 % | 82 % |
| Autarquía estricta | sin ganado | pesca ×3 | 14 % | 38 % | 83 % |
| Autarquía estricta | con ganado | pesca 2021 | 19 % | 44 % | 89 % |
| Autarquía estricta | con ganado | pesca ×3 | 20 % | 46 % | 90 % |
| Insular, insumos actuales | sin ganado | pesca 2021 | 15 % | 49 % | 112 % |
| Insular, insumos actuales | sin ganado | pesca ×3 | 16 % | 51 % | 115 % |
| Insular, insumos actuales | con ganado | pesca 2021 | 22 % | 53 % | 114 % |
| Insular, insumos actuales | con ganado | pesca ×3 | 23 % | 54 % | 115 % |
| Media de España | sin ganado | pesca 2021 | 21 % | 77 % | 165 % |
| Media de España | sin ganado | pesca ×3 | 22 % | 78 % | 166 % |
| Media de España | con ganado | pesca 2021 | 27 % | 78 % | 165 % |
| Media de España | con ganado | pesca ×3 | 28 % | 79 % | 166 % |

Lectura: **ningún escenario pasa del 166 %**. En el de referencia (insumos actuales, 30 % del suelo abandonado recuperado, ganado, pesca de 2021) la cobertura es del 53 %: energía 53 %, proteína 60 %, grasa 53 %, frutas y hortalizas 99 %. La producción actual sin plátano aporta el 12,4 % de la energía y la pesca el 5,1 % de la proteína. [INFERENCIA]

## Reparto del escenario de referencia (insular|0.3|1|1)

| Destino | Dónde | ha / cabezas | Producción | Factor |
|---|---|---:|---:|---:|
| Papa de secano | medianías, secano | 311 | 3.083 t | 0.619 |
| Olivo (aceite) | medianías, secano | 311 | 867 t | 1.087 |
| Almendra | medianías, secano | 156 | 169 t | 2.392 |
| Papa (medianías, regadío) | medianías, regadío | 153 | 3.037 t | 0.619 |
| Cebada (gofio) | medianías, secano | 105 | 132 t | 0.401 |
| Cacahuete | costa, regadío (ex platanera) | 37 | 85 t | 0.7 |
| Millo forrajero (costa) | costa, regadío (ex platanera) | 86 | 1.287 t MS |  |
| Cabra majorera (La Gomera) | establo y monte | 3.678 | 1.471 t leche · 29 t carne |  |

Agua usada: 1,2 de 1,2 hm³. Tierra: 123 ha de costa y 1.037 ha de medianías de las 1.037 recuperables.

## Decisiones (revisables)

1. Frutas y hortalizas como cuarta cobertura en proporción.
2. Techo del monte para el caprino: 0,35 t MS por cabra sobre el máximo del censo ISTAC 2014-2025.
3. Rendimientos: factor por cultivo ISTAC/FAOSTAT (isla, o media de Canarias si la isla no tiene superficie); España = máx(factor, 1); sin dato, 0,7.
4. Dotación del plátano: C por defecto.
5. Pisos climáticos: dos vertientes, regresión de temperatura, mediana de pluviómetros por franja (regresión del logaritmo de la lluvia sobre la cota donde faltan pluviómetros; pendiente regional de Canarias si la isla tiene menos de 3).
6. Viabilidad en el balance (v5): un cultivo de secano (Bs) solo entra si el catálogo lo da VIABLE SECANO o VIABLE CON RIEGO con déficit ≤150 mm; los de regadío (A, Br) si es VIABLE SECANO o VIABLE CON RIEGO. Forraje de secano: 2.59 t MS/ha (3 t/ha con ≥500 mm en el piso más lluvioso, proporcional por debajo).

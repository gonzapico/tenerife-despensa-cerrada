# 04 · Lectura del balance de suficiencia de Lanzarote (v1) [BORRADOR]

Corte: 10/11/2026. Pipeline multi-isla; método y coeficientes de nutrición y ganadería heredados del visor «La Palma, despensa cerrada» v6 y del de Tenerife v4.

## Cifras de partida (C1–C2)

- Residentes: 167.406 (ISTAC, cifras oficiales a 1-1-2025) [VERIFICADO]
- Platanera: 3,7 ha (3 ha bajo invernadero) en el Mapa de Cultivos de Lanzarote 2025 [VERIFICADO]; retenida para consumo local a 15 kg/hab·año [REQUIERE_FUENTE] y 36,1 t/ha: 3,7 ha; liberada: 0,0 ha
- Agua liberada: 0,0 hm³/año con la dotación C (10.000 m³/ha), el 0 % de la demanda agraria de la isla (1,56 hm³). Fuente del agua: Apéndice 1.19 MITECO (PH Lanzarote 3.er ciclo): demanda agraria 1,56 hm³/año, 765 ha regadas [APROXIMADO]; platanera testimonial (4 ha)
- Suelo agrícola no utilizado: 13.457,7 ha; barbecho: 1.833,8 ha (no entra) [VERIFICADO]
- Pesca: 1.300,5 t vendidas en primera venta en puertos de Lanzarote en 2021 [VERIFICADO]
- Censo ganadero 2025 (ISTAC): 22558 caprino, 110 bovino, 4562 ovino, 1406 porcino, 90414 gallinas; techo del monte 7.900 t MS/año [APROXIMADO]
- Necesidades: 2.250 kcal, 55 g de proteína, 70 g de grasa y 400 g de frutas y hortalizas por persona y día [APROXIMADO]

## Pisos climáticos

| Piso | Cota | T media | T mes frío | Mín. abs. est. | Lluvia | Pluviómetros | H. frío |
|---|---|---:|---:|---:|---:|---:|---:|
| P1-N · Costa | 0-150 m | 20,6 °C | 17,3 °C | 11,1 °C | 78 mm | 0 (regresión log-lluvia/cota (isla)) | 0 |
| P2-N · Medianías bajas | 150-300 m | 19,4 °C | 16,1 °C | 10,1 °C | 108 mm | 0 (regresión log-lluvia/cota (isla)) | 4 |
| P3-N · Medianías altas | 300-500 m | 18,1 °C | 14,8 °C | 8,8 °C | 158 mm | 0 (regresión log-lluvia/cota (isla)) | 13 |
| P4-N · Cumbre | 500-671 m | 16,8 °C | 13,5 °C | 7,6 °C | 233 mm | 0 (regresión log-lluvia/cota (isla)) | 64 |
| P1-S · Costa | 0-150 m | 20,6 °C | 17,2 °C | 10,9 °C | 78 mm | 2 (regresión log-lluvia/cota (vertiente)) | 0 |
| P2-S · Medianías bajas | 150-300 m | 19,4 °C | 16,1 °C | 10,0 °C | 108 mm | 2 (regresión log-lluvia/cota (vertiente)) | 4 |
| P3-S · Medianías altas | 300-500 m | 18,1 °C | 14,9 °C | 8,9 °C | 158 mm | 1 (regresión log-lluvia/cota (vertiente)) | 9 |
| P4-S · Cumbre | 500-671 m | 16,7 °C | 13,6 °C | 7,7 °C | 233 mm | 0 (regresión log-lluvia/cota (vertiente)) | 60 |

Temperaturas por regresión sobre la cota con las estaciones de cada vertiente (barlovento N, sotavento S); lluvia por mediana de los pluviómetros de cada franja. vertiente N: menos de 3 estaciones de temperatura; regresión con todas las de la isla Estaciones: 6 de temperatura y 5 pluviómetros. Sesgo de las series cortas frente a las normales: 0.38 °C.

## Rendimientos agrícolas (ISTAC, mediana 2017-2023)

| Cultivo del modelo | Bolsa | FAOSTAT España (kg/ha) | ISTAC (kg/ha) | Factor | Fuente | Viabilidad en la isla (catálogo) |
|---|---|---:|---:|---:|---|---|
| Papa | A | 32.016 | 22.387 | 0.699 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 267 mm) |
| Boniato | A | 12.603 | 10.563 | 0.838 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 517 mm) |
| Millo (grano, gofio) | A | 12.090 | 1.817 | 0.15 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 367 mm) |
| Judía seca | A | 898 | 644 | 0.718 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 267 mm) |
| Ñame | A | 7.480 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 1642 mm) |
| Tomate | A | 81.009 | 48.679 | 0.601 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 367 mm) |
| Col | A | 22.863 | 21.366 | 0.935 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 267 mm) |
| Cebolla | A | 52.967 | 15.485 | 0.292 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 117 mm) |
| Zanahoria | A | 56.126 | 35.000 | 0.624 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 367 mm) |
| Calabaza y bubango | A | 46.204 | 19.668 | 0.426 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 367 mm) |
| Lechuga | A | 28.417 | 41.286 | 1.453 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 867 mm) |
| Plátano (consumo local) | A | 46.313 | 47.040 | 1.016 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 2292 mm) |
| Papaya | A | 31.326 | 59.513 | 1.9 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 1342 mm) |
| Mango | A | 9.818 | 18.971 | 1.932 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 522 mm) |
| Caña de azúcar (miel de caña) | A | 72.000 | 44.430 | 0.617 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 1392 mm) |
| Cacahuete | A | 3.300 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 367 mm) |
| Trigo (gofio) | Bs | 3.399 | 910 | 0.268 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 517 mm) · **excluido** |
| Cebada (gofio) | Bs | 3.136 | 956 | 0.305 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 267 mm) · **excluido** |
| Centeno | Bs | 2.256 | 878 | 0.389 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 367 mm) · **excluido** |
| Garbanzo | Bs | 1.195 | 640 | 0.536 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 367 mm) · **excluido** |
| Lenteja | Bs | 1.228 | 640 | 0.521 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 367 mm) · **excluido** |
| Haba seca | Bs | 1.240 | 667 | 0.538 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 417 mm) · **excluido** |
| Arveja seca | Bs | 1.327 | 551 | 0.415 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 567 mm) · **excluido** |
| Chocho | Bs | 1.500 | 778 | 0.519 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 167 mm) · **excluido** |
| Papa de secano | Bs | 16.008 | 22.387 | 0.699 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 267 mm) · **excluido** |
| Castaña | Bs | 4.733 | 5.033 | 1.063 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 667 mm) · **excluido** |
| Almendra | Bs | 453 | 1.084 | 2.392 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 367 mm) · **excluido** |
| Higo | Bs | 3.100 | 3.447 | 1.112 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 467 mm) · **excluido** |
| Olivo (aceite) | Bs | 2.562 | 4.623 | 1.804 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Girasol (aceite) | Bs | 1.100 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 367 mm) · **excluido** |
| Papa (medianías, regadío) | Br | 32.016 | 22.387 | 0.699 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 267 mm) |
| Millo (medianías, regadío) | Br | 12.090 | 1.817 | 0.15 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 367 mm) |
| Hortalizas (medianías, regadío) | Br | 40.000 | 19.171 | 0.479 | ISTAC 2017-2023, isla | sin entrada en el catálogo (se admite) |

Cultivos del modelo excluidos por el catálogo de la isla (no viables en secano con la lluvia de sus pisos, o no viables): Trigo (gofio) (VIABLE CON RIEGO (déficit 517 mm)); Cebada (gofio) (VIABLE CON RIEGO (déficit 267 mm)); Centeno (VIABLE CON RIEGO (déficit 367 mm)); Garbanzo (VIABLE CON RIEGO (déficit 367 mm)); Lenteja (VIABLE CON RIEGO (déficit 367 mm)); Haba seca (VIABLE CON RIEGO (déficit 417 mm)); Arveja seca (VIABLE CON RIEGO (déficit 567 mm)); Chocho (VIABLE CON RIEGO (déficit 167 mm)); Papa de secano (VIABLE CON RIEGO (déficit 267 mm)); Castaña (VIABLE CON RIEGO (déficit 667 mm)); Almendra (VIABLE CON RIEGO (déficit 367 mm)); Higo (VIABLE CON RIEGO (déficit 467 mm)); Girasol (aceite) (VIABLE CON RIEGO (déficit 367 mm)). [DECISIÓN v5]

## Cobertura mínima en los 132 escenarios

| Insumos | Ganado | Pesca | 0 % SANU | 30 % SANU | 100 % SANU |
|---|---|---|---:|---:|---:|
| Autarquía estricta | sin ganado | pesca 2021 | 3 % | 13 % | 15 % |
| Autarquía estricta | sin ganado | pesca ×3 | 4 % | 14 % | 23 % |
| Autarquía estricta | con ganado | pesca 2021 | 3 % | 16 % | 30 % |
| Autarquía estricta | con ganado | pesca ×3 | 4 % | 17 % | 31 % |
| Insular, insumos actuales | sin ganado | pesca 2021 | 4 % | 18 % | 19 % |
| Insular, insumos actuales | sin ganado | pesca ×3 | 4 % | 19 % | 27 % |
| Insular, insumos actuales | con ganado | pesca 2021 | 4 % | 20 % | 35 % |
| Insular, insumos actuales | con ganado | pesca ×3 | 4 % | 21 % | 38 % |
| Media de España | sin ganado | pesca 2021 | 6 % | 26 % | 32 % |
| Media de España | sin ganado | pesca ×3 | 7 % | 27 % | 40 % |
| Media de España | con ganado | pesca 2021 | 6 % | 30 % | 47 % |
| Media de España | con ganado | pesca ×3 | 7 % | 31 % | 51 % |

Lectura: **ningún escenario pasa del 51 %**. En el de referencia (insumos actuales, 30 % del suelo abandonado recuperado, ganado, pesca de 2021) la cobertura es del 20 %: energía 20 %, proteína 25 %, grasa 28 %, frutas y hortalizas 173 %. La producción actual sin plátano aporta el 11,9 % de la energía y la pesca el 3,9 % de la proteína. [INFERENCIA]

## Reparto del escenario de referencia (insular|0.3|1|1)

| Destino | Dónde | ha / cabezas | Producción | Factor |
|---|---|---:|---:|---:|
| Olivo (aceite) | medianías, secano | 1.211 | 5.598 t | 1.804 |
| Pasto y tagasaste (secano) | medianías, secano | 2.826 | 3.957 t MS |  |
| Cabra majorera | establo y monte | 11.304 | 4.522 t leche · 90 t carne |  |

Agua usada: 0,0 de 0,0 hm³. Tierra: 0 ha de costa y 4.037 ha de medianías de las 4.037 recuperables.

## Decisiones (revisables)

1. Frutas y hortalizas como cuarta cobertura en proporción.
2. Techo del monte para el caprino: 0,35 t MS por cabra sobre el máximo del censo ISTAC 2014-2025.
3. Rendimientos: factor por cultivo ISTAC/FAOSTAT (isla, o media de Canarias si la isla no tiene superficie); España = máx(factor, 1); sin dato, 0,7.
4. Dotación del plátano: C por defecto.
5. Pisos climáticos: dos vertientes, regresión de temperatura, mediana de pluviómetros por franja (regresión del logaritmo de la lluvia sobre la cota donde faltan pluviómetros; pendiente regional de Canarias si la isla tiene menos de 3).
6. Viabilidad en el balance (v5): un cultivo de secano (Bs) solo entra si el catálogo lo da VIABLE SECANO o VIABLE CON RIEGO con déficit ≤150 mm; los de regadío (A, Br) si es VIABLE SECANO o VIABLE CON RIEGO. Forraje de secano: 1.4 t MS/ha (3 t/ha con ≥500 mm en el piso más lluvioso, proporcional por debajo).

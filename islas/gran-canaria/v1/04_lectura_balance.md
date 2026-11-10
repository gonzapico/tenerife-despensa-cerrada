# 04 · Lectura del balance de suficiencia de Gran Canaria (v1) [BORRADOR]

Corte: 10/11/2026. Pipeline multi-isla; método y coeficientes de nutrición y ganadería heredados del visor «La Palma, despensa cerrada» v6 y del de Tenerife v4.

## Cifras de partida (C1–C2)

- Residentes: 870.608 (ISTAC, cifras oficiales a 1-1-2025) [VERIFICADO]
- Platanera: 1.946,7 ha (997 ha bajo invernadero) en el Mapa de Cultivos de Gran Canaria 2024 [VERIFICADO]; retenida para consumo local a 15 kg/hab·año [REQUIERE_FUENTE] y 48,6 t/ha: 266,5 ha; liberada: 1.680,2 ha
- Agua liberada: 16,8 hm³/año con la dotación C (10.000 m³/ha), el 24 % de la demanda agraria de la isla (71,10 hm³). Fuente del agua: Apéndice 1.17 MITECO (PH Gran Canaria 3.er ciclo): demanda agraria 71,1 hm³/año, 8.706 ha regadas [APROXIMADO: tabla fragmentada]; dotación del plátano IPH 10.000 m³/ha
- Suelo agrícola no utilizado: 17.577,4 ha; barbecho: 974,7 ha (no entra) [VERIFICADO]
- Pesca: 1.645,7 t vendidas en primera venta en puertos de Gran Canaria en 2021 [VERIFICADO]
- Censo ganadero 2025 (ISTAC): 41790 caprino, 13865 bovino, 16640 ovino, 5685 porcino, 1027686 gallinas; techo del monte 19.800 t MS/año [APROXIMADO]
- Necesidades: 2.250 kcal, 55 g de proteína, 70 g de grasa y 400 g de frutas y hortalizas por persona y día [APROXIMADO]

## Pisos climáticos

| Piso | Cota | T media | T mes frío | Mín. abs. est. | Lluvia | Pluviómetros | H. frío |
|---|---|---:|---:|---:|---:|---:|---:|
| P1-N · Costa | 0-300 m | 20,0 °C | 17,0 °C | 10,7 °C | 152 mm | 7 (mediana de pluviómetros) | 0 |
| P2-N · Medianías bajas | 300-600 m | 18,8 °C | 15,2 °C | 8,7 °C | 232 mm | 1 (regresión log-lluvia/cota (vertiente)) | 8 |
| P3-N · Medianías altas | 600-1000 m | 17,4 °C | 13,2 °C | 6,3 °C | 332 mm | 2 (regresión log-lluvia/cota (vertiente)) | 75 |
| P4-N · Cumbre baja | 1000-1500 m | 15,7 °C | 10,6 °C | 3,3 °C | 525 mm | 0 (regresión log-lluvia/cota (vertiente)) | 457 |
| P5-N · Cumbre | 1500-1956 m | 13,6 °C | 8,2 °C | 0,3 °C | 832 mm | 1 (regresión log-lluvia/cota (vertiente)) | 1520 |
| P1-S · Costa | 0-300 m | 21,1 °C | 17,7 °C | 11,6 °C | 69 mm | 7 (mediana de pluviómetros) | 0 |
| P2-S · Medianías bajas | 300-600 m | 20,1 °C | 16,1 °C | 9,5 °C | 180 mm | 3 (mediana de pluviómetros) | 4 |
| P3-S · Medianías altas | 600-1000 m | 19,0 °C | 14,2 °C | 7,2 °C | 202 mm | 2 (regresión log-lluvia/cota (vertiente)) | 36 |
| P4-S · Cumbre baja | 1000-1500 m | 17,6 °C | 11,8 °C | 4,1 °C | 347 mm | 1 (regresión log-lluvia/cota (vertiente)) | 203 |
| P5-S · Cumbre | 1500-1956 m | 14,8 °C | 9,0 °C | 0,8 °C | 597 mm | 0 (regresión log-lluvia/cota (vertiente)) | 999 |

Temperaturas por regresión sobre la cota con las estaciones de cada vertiente (barlovento N, sotavento S); lluvia por mediana de los pluviómetros de cada franja.  Estaciones: 23 de temperatura y 24 pluviómetros. Sesgo de las series cortas frente a las normales: 0.38 °C.

## Rendimientos agrícolas (ISTAC, mediana 2017-2023)

| Cultivo del modelo | Bolsa | FAOSTAT España (kg/ha) | ISTAC (kg/ha) | Factor | Fuente | Viabilidad en la isla (catálogo) |
|---|---|---:|---:|---:|---|---|
| Papa | A | 32.016 | 21.791 | 0.681 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Boniato | A | 12.603 | 16.038 | 1.273 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 418 mm) |
| Millo (grano, gofio) | A | 12.090 | 1.936 | 0.16 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 0 mm) |
| Judía seca | A | 898 | 964 | 1.073 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Ñame | A | 7.480 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 1203 mm) |
| Tomate | A | 81.009 | 110.724 | 1.367 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 0 mm) |
| Col | A | 22.863 | 28.763 | 1.258 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Cebolla | A | 52.967 | 22.500 | 0.425 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 0 mm) |
| Zanahoria | A | 56.126 | 32.975 | 0.588 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Calabaza y bubango | A | 46.204 | 46.438 | 1.005 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 0 mm) |
| Lechuga | A | 28.417 | 36.432 | 1.282 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 268 mm) |
| Plátano (consumo local) | A | 46.313 | 48.520 | 1.048 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 2053 mm) |
| Papaya | A | 31.326 | 43.588 | 1.391 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 903 mm) |
| Mango | A | 9.818 | 21.207 | 2.16 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 253 mm) |
| Caña de azúcar (miel de caña) | A | 72.000 | 40.000 | 0.556 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 903 mm) |
| Cacahuete | A | 3.300 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 0 mm) |
| Trigo (gofio) | Bs | 3.399 | 1.378 | 0.405 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Cebada (gofio) | Bs | 3.136 | 1.636 | 0.522 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Centeno | Bs | 2.256 | 1.377 | 0.61 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Garbanzo | Bs | 1.195 | 941 | 0.787 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Lenteja | Bs | 1.228 | 941 | 0.766 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Haba seca | Bs | 1.240 | 956 | 0.771 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 0 mm) |
| Arveja seca | Bs | 1.327 | 1.100 | 0.829 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Chocho | Bs | 1.500 | 778 | 0.519 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 0 mm) |
| Papa de secano | Bs | 16.008 | 21.791 | 0.681 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Castaña | Bs | 4.733 | 2.500 | 0.528 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Almendra | Bs | 453 | 2.084 | 4.6 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Higo | Bs | 3.100 | 11.784 | 3.801 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Olivo (aceite) | Bs | 2.562 | 2.179 | 0.851 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Girasol (aceite) | Bs | 1.100 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 0 mm) |
| Papa (medianías, regadío) | Br | 32.016 | 21.791 | 0.681 | ISTAC 2017-2023, isla | VIABLE SECANO |
| Millo (medianías, regadío) | Br | 12.090 | 1.936 | 0.16 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 0 mm) |
| Hortalizas (medianías, regadío) | Br | 40.000 | 49.152 | 1.229 | ISTAC 2017-2023, isla | sin entrada en el catálogo (se admite) |

Ningún cultivo del modelo queda excluido por el catálogo de la isla.

## Cobertura mínima en los 132 escenarios

| Insumos | Ganado | Pesca | 0 % SANU | 30 % SANU | 100 % SANU |
|---|---|---|---:|---:|---:|
| Autarquía estricta | sin ganado | pesca 2021 | 5 % | 10 % | 19 % |
| Autarquía estricta | sin ganado | pesca ×3 | 5 % | 10 % | 19 % |
| Autarquía estricta | con ganado | pesca 2021 | 8 % | 14 % | 21 % |
| Autarquía estricta | con ganado | pesca ×3 | 8 % | 14 % | 21 % |
| Insular, insumos actuales | sin ganado | pesca 2021 | 6 % | 13 % | 26 % |
| Insular, insumos actuales | sin ganado | pesca ×3 | 6 % | 13 % | 26 % |
| Insular, insumos actuales | con ganado | pesca 2021 | 9 % | 16 % | 26 % |
| Insular, insumos actuales | con ganado | pesca ×3 | 9 % | 16 % | 26 % |
| Media de España | sin ganado | pesca 2021 | 8 % | 19 % | 41 % |
| Media de España | sin ganado | pesca ×3 | 8 % | 19 % | 41 % |
| Media de España | con ganado | pesca 2021 | 10 % | 21 % | 41 % |
| Media de España | con ganado | pesca ×3 | 11 % | 21 % | 41 % |

Lectura: **ningún escenario pasa del 41 %**. En el de referencia (insumos actuales, 30 % del suelo abandonado recuperado, ganado, pesca de 2021) la cobertura es del 16 %: energía 16 %, proteína 20 %, grasa 16 %, frutas y hortalizas 123 %. La producción actual sin plátano aporta el 8,8 % de la energía y la pesca el 0,9 % de la proteína. [INFERENCIA]

## Reparto del escenario de referencia (insular|0.3|1|1)

| Destino | Dónde | ha / cabezas | Producción | Factor |
|---|---|---:|---:|---:|
| Almendra | medianías, secano | 1.582 | 3.297 t | 4.6 |
| Olivo (aceite) | medianías, secano | 1.582 | 3.449 t | 0.851 |
| Girasol (aceite) | medianías, secano | 1.140 | 878 t | 0.7 |
| Plátano (consumo local) | costa, regadío (ex platanera) | 504 | 24.465 t | 1.048 |
| Cacahuete | costa, regadío (ex platanera) | 504 | 1.164 t | 0.7 |
| Tomate | costa, regadío (ex platanera) | 118 | 13.084 t | 1.367 |
| Higo | medianías, secano | 12 | 141 t | 3.801 |
| Forraje regado (medianías) | medianías, regadío | 958 | 11.491 t MS |  |
| Millo forrajero (costa) | costa, regadío (ex platanera) | 554 | 8.309 t MS |  |
| Cabra majorera (Gran Canaria) | establo y monte | 56.571 | 22.629 t leche · 453 t carne |  |

Agua usada: 16,8 de 16,8 hm³. Tierra: 1.680 ha de costa y 5.273 ha de medianías de las 5.273 recuperables.

## Decisiones (revisables)

1. Frutas y hortalizas como cuarta cobertura en proporción.
2. Techo del monte para el caprino: 0,35 t MS por cabra sobre el máximo del censo ISTAC 2014-2025.
3. Rendimientos: factor por cultivo ISTAC/FAOSTAT (isla, o media de Canarias si la isla no tiene superficie); España = máx(factor, 1); sin dato, 0,7.
4. Dotación del plátano: C por defecto.
5. Pisos climáticos: dos vertientes, regresión de temperatura, mediana de pluviómetros por franja (regresión del logaritmo de la lluvia sobre la cota donde faltan pluviómetros; pendiente regional de Canarias si la isla tiene menos de 3).
6. Viabilidad en el balance (v5): un cultivo de secano (Bs) solo entra si el catálogo lo da VIABLE SECANO o VIABLE CON RIEGO con déficit ≤150 mm; los de regadío (A, Br) si es VIABLE SECANO o VIABLE CON RIEGO. Forraje de secano: 3.0 t MS/ha (3 t/ha con ≥500 mm en el piso más lluvioso, proporcional por debajo).

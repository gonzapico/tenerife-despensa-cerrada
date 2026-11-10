# 04 · Lectura del balance de suficiencia de Fuerteventura (v1) [BORRADOR]

Corte: 10/11/2026. Pipeline multi-isla; método y coeficientes de nutrición y ganadería heredados del visor «La Palma, despensa cerrada» v6 y del de Tenerife v4.

## Cifras de partida (C1–C2)

- Residentes: 129.541 (ISTAC, cifras oficiales a 1-1-2025) [VERIFICADO]
- Platanera: 3,0 ha (3 ha bajo invernadero) en el Mapa de Cultivos de Fuerteventura 2025 [VERIFICADO]; retenida para consumo local a 15 kg/hab·año [REQUIERE_FUENTE] y 64,5 t/ha: 3,0 ha; liberada: 0,0 ha
- Agua liberada: 0,0 hm³/año con la dotación C (10.000 m³/ha), el 0 % de la demanda agraria de la isla (1,13 hm³). Fuente del agua: Apéndice 1.18 MITECO (PH Fuerteventura 3.er ciclo): demanda agraria 1,13 hm³/año, 496 ha regadas [APROXIMADO]; platanera testimonial (3 ha)
- Suelo agrícola no utilizado: 7.783,8 ha; barbecho: 588,1 ha (no entra) [VERIFICADO]
- Pesca: 648,7 t vendidas en primera venta en puertos de Fuerteventura en 2021 [VERIFICADO]
- Censo ganadero 2025 (ISTAC): 68174 caprino, 192 bovino, 7755 ovino, 7249 porcino, 15354 gallinas; techo del monte 27.400 t MS/año [APROXIMADO]
- Necesidades: 2.250 kcal, 55 g de proteína, 70 g de grasa y 400 g de frutas y hortalizas por persona y día [APROXIMADO]

## Pisos climáticos

| Piso | Cota | T media | T mes frío | Mín. abs. est. | Lluvia | Pluviómetros | H. frío |
|---|---|---:|---:|---:|---:|---:|---:|
| P1-N · Costa | 0-150 m | 20,9 °C | 17,3 °C | 10,1 °C | 72 mm | 0 (regresión log-lluvia/cota (isla)) | 0 |
| P2-N · Medianías bajas | 150-300 m | 19,6 °C | 16,2 °C | 8,8 °C | 82 mm | 0 (regresión log-lluvia/cota (isla)) | 4 |
| P3-N · Medianías altas | 300-500 m | 18,1 °C | 14,9 °C | 7,3 °C | 95 mm | 0 (regresión log-lluvia/cota (isla)) | 9 |
| P4-N · Cumbre | 500-807 m | 16,2 °C | 13,3 °C | 5,3 °C | 114 mm | 0 (regresión log-lluvia/cota (isla)) | 71 |
| P1-S · Costa | 0-150 m | 20,9 °C | 17,3 °C | 10,1 °C | 61 mm | 3 (mediana de pluviómetros) | 0 |
| P2-S · Medianías bajas | 150-300 m | 19,6 °C | 16,2 °C | 8,8 °C | 82 mm | 2 (regresión log-lluvia/cota (vertiente)) | 4 |
| P3-S · Medianías altas | 300-500 m | 18,1 °C | 14,9 °C | 7,3 °C | 95 mm | 0 (regresión log-lluvia/cota (vertiente)) | 9 |
| P4-S · Cumbre | 500-807 m | 16,2 °C | 13,3 °C | 5,3 °C | 114 mm | 0 (regresión log-lluvia/cota (vertiente)) | 71 |

Temperaturas por regresión sobre la cota con las estaciones de cada vertiente (barlovento N, sotavento S); lluvia por mediana de los pluviómetros de cada franja. vertiente N: menos de 3 estaciones de temperatura; regresión con todas las de la isla Estaciones: 4 de temperatura y 5 pluviómetros. Sesgo de las series cortas frente a las normales: 0.38 °C.

## Rendimientos agrícolas (ISTAC, mediana 2017-2023)

| Cultivo del modelo | Bolsa | FAOSTAT España (kg/ha) | ISTAC (kg/ha) | Factor | Fuente | Viabilidad en la isla (catálogo) |
|---|---|---:|---:|---:|---|---|
| Papa | A | 32.016 | 26.812 | 0.837 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 386 mm) |
| Boniato | A | 12.603 | 11.899 | 0.944 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 636 mm) |
| Millo (grano, gofio) | A | 12.090 | 1.676 | 0.139 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 486 mm) |
| Judía seca | A | 898 | 889 | 0.99 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 386 mm) |
| Ñame | A | 7.480 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 1705 mm) |
| Tomate | A | 81.009 | 73.100 | 0.902 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 486 mm) |
| Col | A | 22.863 | 12.630 | 0.552 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 386 mm) |
| Cebolla | A | 52.967 | 16.150 | 0.305 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 236 mm) |
| Zanahoria | A | 56.126 | 31.798 | 0.567 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 486 mm) |
| Calabaza y bubango | A | 46.204 | 34.040 | 0.737 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 486 mm) |
| Lechuga | A | 28.417 | 37.767 | 1.329 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 986 mm) |
| Plátano (consumo local) | A | 46.313 | 47.040 | 1.016 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 2305 mm) |
| Papaya | A | 31.326 | 59.513 | 1.9 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 1405 mm) |
| Mango | A | 9.818 | 18.971 | 1.932 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 528 mm) |
| Caña de azúcar (miel de caña) | A | 72.000 | 44.430 | 0.617 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 1405 mm) |
| Cacahuete | A | 3.300 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 486 mm) |
| Trigo (gofio) | Bs | 3.399 | 1.008 | 0.297 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 636 mm) · **excluido** |
| Cebada (gofio) | Bs | 3.136 | 1.258 | 0.401 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 386 mm) · **excluido** |
| Centeno | Bs | 2.256 | 878 | 0.389 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 486 mm) · **excluido** |
| Garbanzo | Bs | 1.195 | 676 | 0.565 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 486 mm) · **excluido** |
| Lenteja | Bs | 1.228 | 676 | 0.55 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 486 mm) · **excluido** |
| Haba seca | Bs | 1.240 | 773 | 0.624 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 536 mm) · **excluido** |
| Arveja seca | Bs | 1.327 | 687 | 0.518 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 686 mm) · **excluido** |
| Chocho | Bs | 1.500 | 778 | 0.519 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 286 mm) · **excluido** |
| Papa de secano | Bs | 16.008 | 26.812 | 0.837 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 386 mm) · **excluido** |
| Castaña | Bs | 4.733 | 5.033 | 1.063 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 786 mm) · **excluido** |
| Almendra | Bs | 453 | 1.084 | 2.392 | ISTAC 2017-2023, media de Canarias [APROXIMADO] | VIABLE CON RIEGO (déficit 486 mm) · **excluido** |
| Higo | Bs | 3.100 | 8.891 | 2.868 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 586 mm) · **excluido** |
| Olivo (aceite) | Bs | 2.562 | 2.250 | 0.878 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 286 mm) · **excluido** |
| Girasol (aceite) | Bs | 1.100 | — | 0.7 | FAOSTAT × 0,7 [APROXIMADO] | VIABLE CON RIEGO (déficit 486 mm) · **excluido** |
| Papa (medianías, regadío) | Br | 32.016 | 26.812 | 0.837 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 386 mm) |
| Millo (medianías, regadío) | Br | 12.090 | 1.676 | 0.139 | ISTAC 2017-2023, isla | VIABLE CON RIEGO (déficit 486 mm) |
| Hortalizas (medianías, regadío) | Br | 40.000 | 32.595 | 0.815 | ISTAC 2017-2023, isla | sin entrada en el catálogo (se admite) |

Cultivos del modelo excluidos por el catálogo de la isla (no viables en secano con la lluvia de sus pisos, o no viables): Trigo (gofio) (VIABLE CON RIEGO (déficit 636 mm)); Cebada (gofio) (VIABLE CON RIEGO (déficit 386 mm)); Centeno (VIABLE CON RIEGO (déficit 486 mm)); Garbanzo (VIABLE CON RIEGO (déficit 486 mm)); Lenteja (VIABLE CON RIEGO (déficit 486 mm)); Haba seca (VIABLE CON RIEGO (déficit 536 mm)); Arveja seca (VIABLE CON RIEGO (déficit 686 mm)); Chocho (VIABLE CON RIEGO (déficit 286 mm)); Papa de secano (VIABLE CON RIEGO (déficit 386 mm)); Castaña (VIABLE CON RIEGO (déficit 786 mm)); Almendra (VIABLE CON RIEGO (déficit 486 mm)); Higo (VIABLE CON RIEGO (déficit 586 mm)); Olivo (aceite) (VIABLE CON RIEGO (déficit 286 mm)); Girasol (aceite) (VIABLE CON RIEGO (déficit 486 mm)). [DECISIÓN v5]

## Cobertura mínima en los 132 escenarios

| Insumos | Ganado | Pesca | 0 % SANU | 30 % SANU | 100 % SANU |
|---|---|---|---:|---:|---:|
| Autarquía estricta | sin ganado | pesca 2021 | 3 % | 3 % | 3 % |
| Autarquía estricta | sin ganado | pesca ×3 | 3 % | 3 % | 3 % |
| Autarquía estricta | con ganado | pesca 2021 | 3 % | 5 % | 8 % |
| Autarquía estricta | con ganado | pesca ×3 | 3 % | 6 % | 9 % |
| Insular, insumos actuales | sin ganado | pesca 2021 | 4 % | 4 % | 4 % |
| Insular, insumos actuales | sin ganado | pesca ×3 | 4 % | 4 % | 4 % |
| Insular, insumos actuales | con ganado | pesca 2021 | 4 % | 6 % | 10 % |
| Insular, insumos actuales | con ganado | pesca ×3 | 4 % | 7 % | 10 % |
| Media de España | sin ganado | pesca 2021 | 5 % | 5 % | 5 % |
| Media de España | sin ganado | pesca ×3 | 5 % | 5 % | 5 % |
| Media de España | con ganado | pesca 2021 | 5 % | 7 % | 11 % |
| Media de España | con ganado | pesca ×3 | 5 % | 8 % | 12 % |

Lectura: **ningún escenario pasa del 12 %**. En el de referencia (insumos actuales, 30 % del suelo abandonado recuperado, ganado, pesca de 2021) la cobertura es del 6 %: energía 7 %, proteína 11 %, grasa 6 %, frutas y hortalizas 52 %. La producción actual sin plátano aporta el 5,2 % de la energía y la pesca el 2,5 % de la proteína. [INFERENCIA]

## Reparto del escenario de referencia (insular|0.3|1|1)

| Destino | Dónde | ha / cabezas | Producción | Factor |
|---|---|---:|---:|---:|
| Pasto y tagasaste (secano) | medianías, secano | 2.335 | 1.588 t MS |  |
| Cabra majorera | establo y monte | 4.537 | 1.815 t leche · 36 t carne |  |

Agua usada: 0,0 de 0,0 hm³. Tierra: 0 ha de costa y 2.335 ha de medianías de las 2.335 recuperables.

## Decisiones (revisables)

1. Frutas y hortalizas como cuarta cobertura en proporción.
2. Techo del monte para el caprino: 0,35 t MS por cabra sobre el máximo del censo ISTAC 2014-2025.
3. Rendimientos: factor por cultivo ISTAC/FAOSTAT (isla, o media de Canarias si la isla no tiene superficie); España = máx(factor, 1); sin dato, 0,7.
4. Dotación del plátano: C por defecto.
5. Pisos climáticos: dos vertientes, regresión de temperatura, mediana de pluviómetros por franja (regresión del logaritmo de la lluvia sobre la cota donde faltan pluviómetros; pendiente regional de Canarias si la isla tiene menos de 3).
6. Viabilidad en el balance (v5): un cultivo de secano (Bs) solo entra si el catálogo lo da VIABLE SECANO o VIABLE CON RIEGO con déficit ≤150 mm; los de regadío (A, Br) si es VIABLE SECANO o VIABLE CON RIEGO. Forraje de secano: 0.68 t MS/ha (3 t/ha con ≥500 mm en el piso más lluvioso, proporcional por debajo).

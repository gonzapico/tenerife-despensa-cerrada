# 04 · Lectura del balance de suficiencia de Tenerife (v3) [BORRADOR]

Corte: 06/11/2026. Método y coeficientes de rendimiento, nutrición y ganadería heredados del visor «La Palma, despensa cerrada» v6; tierra, agua, población, pesca, censo y clima de fuentes directas de Tenerife.

## Cifras de partida (C1–C2)

- Residentes: 961.745 (ISTAC, cifras oficiales a 1-1-2025) [VERIFICADO]
- Platanera: 3.935,1 ha, el 100 % con riego y 1.448 ha bajo invernadero (Mapa de Cultivos de Tenerife 2021) [VERIFICADO]; retenida para consumo local a 15 kg/hab·año [REQUIERE_FUENTE] y 44 t/ha [APROXIMADO]: 327,9 ha; liberada: 3.607,2 ha
- Agua liberada: 24,7 hm³/año con la dotación media del regadío (6.846 m³/ha = 84,23 hm³ consumidos en regadío en 2016 / 12.304 ha regadas en 2021, memoria del Plan Hidrológico) [VERIFICADO el origen; la dotación específica del plátano no figura]; 31,6–42,1 hm³ por consumo por planta
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

## Cobertura mínima (energía, proteína, grasa y frutas y hortalizas) en los 132 escenarios

| Insumos | Ganado | Pesca | 0 % SANU | 30 % SANU | 100 % SANU |
|---|---|---|---:|---:|---:|
| Autarquía estricta | sin ganado | pesca 2021 | 6 % | 11 % | 20 % |
| Autarquía estricta | sin ganado | pesca ×3 | 6 % | 11 % | 21 % |
| Autarquía estricta | con ganado | pesca 2021 | 9 % | 14 % | 22 % |
| Autarquía estricta | con ganado | pesca ×3 | 9 % | 15 % | 22 % |
| Insular, insumos actuales | sin ganado | pesca 2021 | 6 % | 13 % | 26 % |
| Insular, insumos actuales | sin ganado | pesca ×3 | 7 % | 14 % | 27 % |
| Insular, insumos actuales | con ganado | pesca 2021 | 9 % | 16 % | 27 % |
| Insular, insumos actuales | con ganado | pesca ×3 | 10 % | 16 % | 28 % |
| Media de España | sin ganado | pesca 2021 | 9 % | 19 % | 37 % |
| Media de España | sin ganado | pesca ×3 | 9 % | 20 % | 38 % |
| Media de España | con ganado | pesca 2021 | 12 % | 21 % | 38 % |
| Media de España | con ganado | pesca ×3 | 12 % | 22 % | 38 % |

Lectura: **ningún escenario pasa del 38 %**. En el de referencia (insumos actuales, 30 % del suelo abandonado recuperado, ganado, pesca de 2021) la cobertura es del 16 %: energía 17 %, proteína 22 %, grasa 16 %, frutas y hortalizas 16 %. La producción actual sin plátano aporta el 1,1 % de la energía y la pesca el 2,2 % de la proteína. [INFERENCIA]

## Reparto del escenario de referencia (insular|0.3|1|1)

| Destino | Dónde | ha / cabezas | Producción |
|---|---|---:|---:|
| Olivo (aceite) | medianías, secano | 1.729 | 3.102 t |
| Girasol (aceite) | medianías, secano | 1.729 | 1.332 t |
| Millo (medianías, regadío) | medianías, regadío | 1.729 | 14.636 t |
| Millo (grano, gofio) | costa, regadío (ex platanera) | 1.082 | 9.158 t |
| Cacahuete | costa, regadío (ex platanera) | 1.082 | 2.500 t |
| Chocho | medianías, secano | 576 | 605 t |
| Cebolla | costa, regadío (ex platanera) | 387 | 14.334 t |
| Tomate | costa, regadío (ex platanera) | 17 | 961 t |
| Millo forrajero (costa) | costa, regadío (ex platanera) | 1.039 | 15.590 t MS |
| Cabra tinerfeña | establo y monte | 37.143 | 14.857 t leche · 297 t carne |
| Vaca de leche | establo y monte | 398 | 1.793 t leche · 24 t carne |

Agua usada: 24,7 de 24,7 hm³. Tierra: 3.607 ha de costa y 5.765 ha de medianías de las 5.765 recuperables. El caprino está limitado por el monte (13.000 t MS/año, calibrado con el máximo del censo ISTAC 2014-2025).

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

## Decisiones de la v3 (revisables)

1. Frutas y hortalizas como cuarta cobertura en proporción.
2. Techo del monte para el caprino: 13.000 t de materia seca al año.
3. Coeficientes de leche y carne de la cabra palmera aplicados a la cabra tinerfeña.
4. Ni el barbecho ni el suelo abandonado con riego entran aparte en la bolsa recuperable.
5. Pisos climáticos: dos vertientes, regresión de temperatura por debajo de 1.300 m, mediana de pluviómetros por franja.

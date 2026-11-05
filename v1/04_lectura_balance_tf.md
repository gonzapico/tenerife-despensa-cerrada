# 04 · Lectura del balance de suficiencia de Tenerife (v1) [BORRADOR]

Corte: 05/11/2026. Método y coeficientes heredados del visor «La Palma, despensa cerrada» v6; cambian la tierra, el agua, la población, la pesca y el techo del monte.

## Cifras de partida (C1–C2)

- Residentes: 955.063 (ISTAC, cifra provisional a 1-1-2025) [APROXIMADO]
- Platanera: 3.935,1 ha (Mapa de Cultivos de Tenerife 2020-21) [VERIFICADO]; retenida para consumo local a 15 kg/hab·año y 44 t/ha: 325,6 ha; liberada: 3.609,5 ha
- Agua liberada: 25,6 hm³/año con la dotación media del regadío (7.080 m³/ha = 84,25 hm³ / 11.900 ha del Plan Hidrológico, 3.er ciclo) [APROXIMADO]; 31,6–42,2 hm³ por consumo por planta
- Suelo agrícola no utilizado: 19.215,9 ha; barbecho: 2.382,2 ha (no entra en v1) [VERIFICADO]
- Pesca: 3.500 t/año (Cabildo de Tenerife, sin año) [APROXIMADO]
- Necesidades: 2.250 kcal, 55 g de proteína, 70 g de grasa y 400 g de frutas y hortalizas por persona y día [APROXIMADO]

## Cobertura mínima (energía, proteína, grasa y frutas y hortalizas) en los 132 escenarios

| Insumos | Ganado | Pesca | 0 % SANU | 30 % SANU | 100 % SANU |
|---|---|---|---:|---:|---:|
| Autarquía estricta | sin ganado | pesca 2021-24 | 6 % | 11 % | 20 % |
| Autarquía estricta | sin ganado | pesca ×3 | 6 % | 11 % | 21 % |
| Autarquía estricta | con ganado | pesca 2021-24 | 9 % | 15 % | 23 % |
| Autarquía estricta | con ganado | pesca ×3 | 10 % | 16 % | 23 % |
| Insular, insumos actuales | sin ganado | pesca 2021-24 | 6 % | 13 % | 27 % |
| Insular, insumos actuales | sin ganado | pesca ×3 | 7 % | 14 % | 27 % |
| Insular, insumos actuales | con ganado | pesca 2021-24 | 9 % | 17 % | 28 % |
| Insular, insumos actuales | con ganado | pesca ×3 | 10 % | 17 % | 28 % |
| Media de España | sin ganado | pesca 2021-24 | 9 % | 19 % | 38 % |
| Media de España | sin ganado | pesca ×3 | 9 % | 20 % | 38 % |
| Media de España | con ganado | pesca 2021-24 | 12 % | 22 % | 38 % |
| Media de España | con ganado | pesca ×3 | 13 % | 22 % | 39 % |

Lectura: **ningún escenario pasa del 39 %**. En el de referencia (insumos actuales, 30 % del suelo abandonado recuperado, ganado, pesca actual) la cobertura es del 17 %: energía 17 %, proteína 22 %, grasa 17 %, frutas y hortalizas 17 %. La producción actual sin plátano aporta el 1,1 % de la energía y la pesca el 1,8 % de la proteína. [INFERENCIA]

## Reparto del escenario de referencia (insular|0.3|1|1)

| Destino | Dónde | ha / cabezas | Producción |
|---|---|---:|---:|
| Olivo (aceite) | medianías, secano | 1.729 | 3.102 t |
| Girasol (aceite) | medianías, secano | 1.729 | 1.332 t |
| Millo (medianías, regadío) | medianías, regadío | 1.583 | 13.399 t |
| Cacahuete | costa, regadío (ex platanera) | 1.083 | 2.501 t |
| Millo (grano, gofio) | costa, regadío (ex platanera) | 1.063 | 8.997 t |
| Tomate | costa, regadío (ex platanera) | 275 | 15.577 t |
| Millo forrajero (costa) | costa, regadío (ex platanera) | 1.189 | 17.832 t MS |
| Pasto y tagasaste (secano) | medianías, secano | 723 | 2.168 t MS |
| Cabra tinerfeña | establo y monte | 57.143 | 22.857 t leche · 457 t carne |

Agua usada: 25,6 de 25,6 hm³. Tierra: 3.610 ha de costa y 5.765 ha de medianías de las 5.765 recuperables.

## La Palma frente a Tenerife

| | La Palma (v6) | Tenerife (v1) |
|---|---:|---:|
| Residentes | 86.194 | 955.063 |
| Platanera (ha) | 2.675 | 3.935 |
| Platanera retenida para consumo local (ha) | 29 | 326 |
| Tierra liberada (ha) | 2.646 | 3.609 |
| Agua liberada, dotación media (hm³/año) | 22,4 | 25,6 |
| Demanda agraria de la isla (hm³/año) | 41,1 | 84,25 |
| Suelo agrícola abandonado (ha) | 7.645 | 19.216 |
| Hectáreas cultivadas o abandonadas por cada 1.000 residentes | 162,0 | 40,6 |
| Pesca de partida (t/año) | 190 | 3.500 |
| Cobertura mínima, insumos actuales, 30 % SANU, ganado | 110 % | 17 % |
| Cobertura mínima, mejor caso (España, 100 % SANU, pesca ×3) | 257 % | 39 % |

La diferencia no está en el clima ni en la nevera: está en la escala. Tenerife tiene once veces más residentes y solo 1,5 veces más platanera. [INFERENCIA]

## Decisiones de la v1 (revisables)

1. Frutas y hortalizas como cuarta cobertura en proporción (una obligación absoluta de 400 g/día ocupa toda la costa y baja la cobertura mínima al 15 %).
2. Techo del monte para el caprino: 20.000 t de materia seca al año; sin él, el modelo pone más de 200.000 cabras. Con él, el orden del censo real (56.704 cabras en 2010).
3. Las cabras se llaman «cabra tinerfeña»; coeficientes de leche y carne, los de la cabra palmera.
4. El barbecho no entra en la bolsa de tierra recuperable.

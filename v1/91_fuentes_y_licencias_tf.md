# 91 · Fuentes, licencias y etiquetas (v1) [BORRADOR]

| F | Fuente | Uso | Licencia | Estado |
|---|---|---|---|---|
| F1 | Mapa de Cultivos de Tenerife 2020-21, Gobierno de Canarias. Copia GeoParquet de fiboa / Fields of the World en Source Cooperative (`s3://us-west-2.opendata.source.coop/fiboa/es-cn/es_cn.parquet`, descargada el 05/11/2026). 177.543 parcelas, 38.728 ha | parcelas, superficies, suelo abandonado | CC BY 4.0 | [VERIFICADO] (copia; falta cotejar con opendata.sitcan.es) |
| F2 | Copernicus DEM GLO-30, tesela N28 W017 (`copernicus-dem-30m` en AWS) | relieve, cota y pendiente de cada parcela | © DLR/Airbus, Copernicus (UE/ESA), uso libre con atribución | [VERIFICADO] |
| F3 | FAO ECOCROP, copia pública en github.com/OpenCLIM/ecocrop (EcoCrop_DB.csv) | requisitos de temperatura y lluvia; solo cálculo | FAO; copia bajo OGL v3 | [VERIFICADO] el origen |
| F4 | Universo de productos FAOSTAT 2024 y variedades locales, heredados del visor de La Palma | catálogo | CC BY 4.0 | [VERIFICADO] |
| F5 | Normales climatológicas AEMET (Santa Cruz, Los Rodeos, Reina Sofía, Izaña) y gradiente por vertientes | 10 pisos climáticos | AEMET | [CONOCIMIENTO_BASE] · pendiente descarga de AEMET OpenData (bloqueado en la sesión) |
| F6 | ISTAC, cifra provisional de población de Tenerife a 1-1-2025 (955.063), vía prensa | residentes | — | [APROXIMADO] · la cifra revisada no se pudo consultar (ISTAC bloqueado) |
| F7 | Plan Hidrológico de Tenerife, 3.er ciclo (apéndice 1.20 de MITECO, 2021): demanda agraria 84,25 hm³ y 11.794-12.144 ha regadas | dotación media y demanda | — | [APROXIMADO] · tabla fragmentada; aguastenerife.org bloqueado |
| F8 | Cabildo de Tenerife, «La pesca en Tenerife»: 3.500-3.800 t/año | pesca | — | [APROXIMADO] · sin año ni especies |
| F9 | Rendimientos (FAOSTAT España 2020-24 o mundo 2024), composición nutricional, coeficientes de ganado y nitrógeno | balance | heredados de La Palma | [APROXIMADO]/[CONOCIMIENTO_BASE] · sin adaptar a Tenerife |
| F10 | Censo caprino de Tenerife 2010 (56.704 cabras), vía prensa | calibración del techo del monte | — | [APROXIMADO] |
| F11 | Temporadas, platos, pescados, antecedentes de la cocina y el botiquín | escenas 5-7 | — | [CONOCIMIENTO_BASE] |

Dominios que la red de la sesión bloqueó: datos.canarias.es, opendata.sitcan.es, idecan*.grafcan.es, www.ine.es, www.istac.es / www3.gobiernodecanarias.org, opendata.aemet.es, aguastenerife.org, www.gobiernodecanarias.org, datos.gob.es, fao.org, wikipedia.org, archive.org, fiboa.org, huggingface.co.

Etiquetas: [VERIFICADO] dato leído de su fuente; [APROXIMADO] cifra de segunda mano o redondeada; [INFERENCIA] resultado del modelo o del criterio propio; [REQUIERE_FUENTE] sin acreditar; [CONOCIMIENTO_BASE] aportado de memoria por la IA.

Licencias de la obra: textos, ilustraciones y código propios, reutilizables citando la fuente; three.js (MIT) incrustado; datos con la licencia de su titular.

# 91 · Fuentes, licencias y etiquetas · Gran Canaria (v1) [BORRADOR]

| F | Fuente | Uso | Licencia | Estado |
|---|---|---|---|---|
| F1 | Mapa de Cultivos de Gran Canaria 2024, Gobierno de Canarias (`opendata.sitcan.es/upload/medio-rural/gobcan_mapa-cultivos_*_shp.zip`, fichero GC_MCultivos_2024.shp). 104.976 parcelas, 28.440 ha; campos CULTIVO, REGADIO, ABANDON, TECNICA | parcelas, superficies, riego, suelo abandonado, calibración | CC BY 4.0 | [VERIFICADO] |
| F2 | Copernicus DEM GLO-30, teselas N27_00_W016_00, N28_00_W016_00 (`copernicus-dem-30m` en AWS) | relieve, cota y pendiente | © DLR/Airbus, Copernicus (UE/ESA), uso libre con atribución | [VERIFICADO] |
| F3 | FAO ECOCROP, copia pública en github.com/OpenCLIM/ecocrop | requisitos de temperatura y lluvia; solo cálculo | FAO; copia bajo OGL v3 | [VERIFICADO] el origen |
| F4 | Universo FAOSTAT 2024 y variedades locales, heredados del visor de La Palma | catálogo | CC BY 4.0 | [VERIFICADO] |
| F5 | AEMET OpenData: normales 1991-2020 y series mensuales 2009-2025 de las estaciones de la isla (26 usadas, ver 92c_pisos_salida.json) | pisos climáticos | AEMET, citar como autora | [VERIFICADO] el origen; series cortas [APROXIMADO] |
| F6 | ISTAC, Cifras oficiales de población, municipios por islas (E30245A_000002, 15/12/2025): Gran Canaria 870.608 a 1-1-2025 | residentes | ISTAC | [VERIFICADO] |
| F7 | Apéndice 1.17 MITECO (PH Gran Canaria 3.er ciclo): demanda agraria 71,1 hm³/año, 8.706 ha regadas [APROXIMADO: tabla fragmentada]; dotación del plátano IPH 10.000 m³/ha | dotación y demanda agraria | — | ver etiquetas en la fuente |
| F8 | Gobierno de Canarias, Registro de primera venta de productos pesqueros 2021 (datos.canarias.es): 1.645,7 t en puertos de Gran Canaria | pesca, especies y meses | CC BY 4.0 | [VERIFICADO]; solo 2021 publicado |
| F9 | ISTAC, Efectivos de ganado según especies, islas 2014-2025 (E01008B_000001) | calibración del techo del monte | ISTAC | [VERIFICADO] |
| F10 | Composición nutricional y coeficientes de ganado, forraje y nitrógeno | balance | heredados de La Palma | [APROXIMADO]/[CONOCIMIENTO_BASE] |
| F11 | Nevera, despensa, menú y botiquín: base canaria y particularidades de la isla (pipeline/cocina_islas.json) | escenas 5-7 | — | [CONOCIMIENTO_BASE] |
| F12 | ISTAC, Estadística anual de superficies y producciones de cultivos (E01135A_000003/4/5), Gran Canaria y Canarias, mediana 2017-2023 | rendimientos por cultivo y de la platanera | ISTAC | [VERIFICADO] |

Etiquetas: [VERIFICADO] dato leído de su fuente; [APROXIMADO] cifra de segunda mano o redondeada; [INFERENCIA] resultado del modelo o del criterio propio; [REQUIERE_FUENTE] sin acreditar; [CONOCIMIENTO_BASE] aportado de memoria por la IA.

Licencias de la obra: código MIT; textos, ilustraciones y datos derivados CC BY 4.0 (ver LICENSE y LICENSE-CONTENIDO.md en la raíz del repositorio); three.js (MIT) incrustado; datos con la licencia de su titular.

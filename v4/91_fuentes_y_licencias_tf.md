# 91 · Fuentes, licencias y etiquetas (v4) [BORRADOR]

| F | Fuente | Uso | Licencia | Estado |
|---|---|---|---|---|
| F1 | Mapa de Cultivos de Tenerife 2021, Gobierno de Canarias (`opendata.sitcan.es/upload/medio-rural/gobcan_mapa-cultivos_tf_shp.zip`, fichero de 21/03/2022, campo enero-mayo 2021). 177.543 parcelas, 38.728 ha; campos CULTIVO, REGADIO, ABANDON, TECNICA, CATEGORIA. Idéntico a la copia de fiboa usada en v1 | parcelas, superficies, riego, suelo abandonado, calibración | CC BY 4.0 | [VERIFICADO] |
| F2 | Copernicus DEM GLO-30, tesela N28 W017 (`copernicus-dem-30m` en AWS) | relieve, cota y pendiente | © DLR/Airbus, Copernicus (UE/ESA), uso libre con atribución | [VERIFICADO] |
| F3 | FAO ECOCROP, copia pública en github.com/OpenCLIM/ecocrop | requisitos de temperatura y lluvia; solo cálculo | FAO; copia bajo OGL v3 | [VERIFICADO] el origen |
| F4 | Universo FAOSTAT 2024 y variedades locales, heredados del visor de La Palma | catálogo | CC BY 4.0 | [VERIFICADO] |
| F5 | AEMET OpenData (clave propia): valores climatológicos normales 1991-2020 y series mensuales 2007-2025 de las 16 estaciones de Tenerife (`datos_clima/aemet_*`) | pisos climáticos: temperatura, mínima absoluta y lluvia | AEMET, citar como autora | [VERIFICADO]; las automáticas tienen 4-17 años de serie [APROXIMADO] |
| F5b | Cabildo de Tenerife, Agrocabildo: «Temperatura del aire, análisis 2008» (40 estaciones, medias 2001-2007) y L. M. Santana Pérez (2012) «¿Existe cambio pluviométrico en los últimos 40 años en Tenerife?» (224 pluviómetros por transectos, 1983-2010) (`datos_clima/agrocabildo_*`) | pisos climáticos: lapso térmico y lluvia por franja | Cabildo de Tenerife, publicaciones divulgativas | [VERIFICADO] el origen; periodos cortos y heterogéneos [APROXIMADO] |
| F6 | ISTAC, Cifras oficiales de población, municipios por islas (E30245A_000002, 15/12/2025): Tenerife 961.745 a 1-1-2025 | residentes | ISTAC, reutilización libre con cita | [VERIFICADO] |
| F7 | Consejo Insular de Aguas de Tenerife, memoria del Plan Hidrológico 3.er ciclo (feb. 2023): consumo en regadío 84,23 hm³ (2016, BHITF), 12.304 ha regadas (2021), demanda 2027-2033 85,7 hm³, dosis de N por cultivo (platanera 250 kg/ha) | dotación media y demanda | — | [VERIFICADO]; la dotación específica del plátano no figura |
| F8 | Gobierno de Canarias, Registro de primera venta de productos pesqueros 2021 (datos.canarias.es): 4.278,7 t en puertos de Tenerife | pesca, especies y meses | CC BY 4.0 | [VERIFICADO]; solo 2021 publicado |
| F9 | ISTAC, Efectivos de ganado según especies, municipios e islas 2014-2025 (E01008B_000001): caprino 28.452 (2025), máximo 37.253 (2014) | calibración del techo del monte | ISTAC | [VERIFICADO] |
| F10 | Composición nutricional y coeficientes de ganado, forraje y nitrógeno | balance | heredados de La Palma | [APROXIMADO]/[CONOCIMIENTO_BASE] · sin adaptar a Tenerife |
| F12 | ISTAC, Estadística anual de superficies y producciones de cultivos: producción recolectada (E01135A_000005), superficie cultivada de herbáceos (E01135A_000003) y de producción de permanentes (E01135A_000004), Tenerife 2017-2023 (`datos_agrarios/istac_rendimientos_tenerife_2017-2023.csv`) | rendimientos por cultivo y de la platanera | ISTAC | [VERIFICADO] |
| F13 | Cabildo de Tenerife, Estudio de Consumos Hídricos (2005), citado por C. Méndez Hernández, «Recomendaciones de riego en Tenerife» (UIMP): 12.375 m³/ha·año, 60 % del agua agraria; IPH de Canarias, dotación del plátano 10.000 m³/ha reproducida en la normativa del PH de Lanzarote (`datos_agrarios/`) | agua liberada por la platanera | — | [VERIFICADO el origen] / [APROXIMADO] |
| F11 | Temporadas de huerta y fruta, platos, antecedentes de la cocina y el botiquín | escenas 5-7 | — | [CONOCIMIENTO_BASE] |

Dominios que siguen bloqueados en la sesión: www.tenerife.es, bancodatos.tenerife.es. Grafcan no expone un WFS de límites municipales (solo WMS). Los ficheros de referencia externos (plantilla de La Palma, ECOCROP, DEM) viven en `../_ref/`, fuera del repositorio.

Etiquetas: [VERIFICADO] dato leído de su fuente; [APROXIMADO] cifra de segunda mano o redondeada; [INFERENCIA] resultado del modelo o del criterio propio; [REQUIERE_FUENTE] sin acreditar; [CONOCIMIENTO_BASE] aportado de memoria por la IA.

Licencias de la obra: textos, ilustraciones y código propios, reutilizables citando la fuente; three.js (MIT) incrustado; datos con la licencia de su titular.

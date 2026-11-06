# Tenerife, despensa cerrada · v3 (06/11/2026) [BORRADOR]

Réplica para Tenerife del visor «La Palma, despensa cerrada» (territorio.visualizalapalma.es/p/despensa-cerrada/) y de su página de carga pendiente (/p/despensa-pendiente/). v3: el clima por pisos sale de estaciones reales (AEMET OpenData y Agrocabildo) en vez de una interpolación entre siete puntos. La v1 y la v2 se conservan en `../v1` y `../v2`.

## Piezas firmables (00–05)
- `00_INDICE.md` · este fichero · `01_RESUMEN.md` · resumen ejecutivo en cinco puntos
- `03_catalogo_viabilidad_tf.csv` · catálogo de 164 productos por pisos (salida de 93)
- `04_lectura_balance_tf.md` · escenarios, cifras, cambios v1→v2 y comparación con La Palma
- `04b_cocina_tf.json` · nevera, despensa, menú y botiquín (salida de 04b; pescado del registro de 2021)
- `05_visor_despensa_cerrada_tf_v3.html` · **el visor** (1,8 MB, un solo HTML, sin red) · `aviso_tf.html` · aviso, fuentes y licencias

## Soporte (90–99)
- `90_verificacion_tf.csv` · pruebas que pasan · `90_test_visor.js`, `90_test_pendiente.js`, `90_test_resultado.json`
- `91_fuentes_y_licencias_tf.md` · fuentes F1–F11 y etiquetas
- `92c_pisos_climaticos_tf.py` → `92c_pisos_salida_tf.json` · diez pisos climáticos a partir de `datos_clima/` (AEMET y Agrocabildo)
- `93_catalogo_viabilidad_tf.py` → `95_catalogo_salida_tf.json` · reglas ECOCROP y calibración con REGADIO sobre los pisos de 92c
- `96_balance_suficiencia_tf.py` → `97_balance_salida_tf.json` · C1-C2 y rejilla de 132 escenarios
- `93c_territorio_tf.py` → `94_territorio_salida_tf.json`, `tex_hoy_tf.jpg`, `tex_fut_tf.jpg`
- `98_ensamblar_visor_tf.py` · monta el visor sobre la plantilla de La Palma · `99_carga_pendiente_tf.py` → `99_CARGA_PENDIENTE_TF.html`
- `datos_clima/` · normales y series de AEMET (CSV y JSON brutos) y tablas de Agrocabildo (CSV)
- `mapa_oficial_resumen.json`, `istac_resumen.json`, `pesca_tf_2021.json`, `clima_wiki.json` · extractos de las fuentes
- `_dl/tf_parcelas_mapa_cultivos_2021_oficial.parquet` · parcelas oficiales con cota y pendiente (67 MB)
- `_capturas/` · capturas de las pruebas

## Cómo rehacerlo
```
pip install geopandas pyogrio rasterio scipy pandas pillow
python3 92c_pisos_climaticos_tf.py && python3 93_catalogo_viabilidad_tf.py && python3 96_balance_suficiencia_tf.py && python3 93c_territorio_tf.py && python3 04b_cocina_tf.py && python3 98_ensamblar_visor_tf.py && python3 99_carga_pendiente_tf.py
node 90_test_visor.js 05_visor_despensa_cerrada_tf_v3.html
```
Ficheros de referencia externos (no versionados), en `../_ref/` o en la ruta de la variable `DESPENSA_REF`: `lapalma_D.json` y `lapalma_visor.html` y `lapalma_despensa_pendiente.html` (plantilla del visor de La Palma, territorio.visualizalapalma.es), `EcoCrop_DB.csv` (github.com/OpenCLIM/ecocrop) y `tf_dem_N28_W017.tif` (Copernicus DEM GLO-30, AWS). Las parcelas (`tf_parcelas_v2.parquet`) se regeneran con el script de v2 a partir del shapefile de opendata.sitcan.es.
```
```

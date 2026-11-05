# Tenerife, despensa cerrada · v1 (05/11/2026) [BORRADOR]

Réplica para Tenerife del visor «La Palma, despensa cerrada» (territorio.visualizalapalma.es/p/despensa-cerrada/) y de su página de carga pendiente (/p/despensa-pendiente/). Generada en una sesión de Claude Code.

## Piezas firmables (00–05)
- `00_INDICE.md` · este fichero
- `01_RESUMEN.md` · resumen ejecutivo en cinco puntos
- `03_catalogo_viabilidad_tf.csv` · catálogo de 164 productos clasificados por pisos (salida de 93)
- `04_lectura_balance_tf.md` · escenarios, cifras del balance y comparación con La Palma
- `04b_cocina_tf.json` · nevera, despensa, menú y botiquín (salida de 04b)
- `05_visor_despensa_cerrada_tf_v1.html` · **el visor** (1,8 MB, un solo HTML, sin red) · `aviso_tf.html` · aviso, fuentes y licencias

## Soporte (90–99)
- `90_verificacion_tf.csv` · pruebas que pasan · `90_test_visor.js`, `90_test_pendiente.js`, `90_test_resultado.json` · pruebas Playwright
- `91_fuentes_y_licencias_tf.md` · fuentes, etiquetas y dominios bloqueados
- `93_catalogo_viabilidad_tf.py` → `95_catalogo_salida_tf.json` · pisos climáticos, reglas ECOCROP y calibración
- `96_balance_suficiencia_tf.py` → `97_balance_salida_tf.json` · C1-C2 y rejilla de 132 escenarios (programación lineal)
- `93c_territorio_tf.py` → `94_territorio_salida_tf.json`, `tex_hoy_tf.jpg`, `tex_fut_tf.jpg` · malla 3D y texturas
- `98_ensamblar_visor_tf.py` · monta el visor sobre la plantilla de La Palma
- `99_carga_pendiente_tf.py` → `99_CARGA_PENDIENTE_TF.html` · la presentación de deuda y el prompt de reinicio
- `_dl/tf_parcelas_mapa_cultivos_2020-21.parquet` · parcelas de Tenerife con cota y pendiente (derivado de F1 y F2)
- `_capturas/` · capturas de las pruebas

## Cómo rehacerlo
```
pip install geopandas pyogrio rasterio scipy pandas pillow
python3 93_catalogo_viabilidad_tf.py && python3 96_balance_suficiencia_tf.py && python3 93c_territorio_tf.py && python3 04b_cocina_tf.py && python3 98_ensamblar_visor_tf.py && python3 99_carga_pendiente_tf.py
node 90_test_visor.js 05_visor_despensa_cerrada_tf_v1.html
```
Los scripts leen la plantilla del visor de La Palma (`visor.html` y `page.html` descargados del sitio) y las descargas de F1-F3; las rutas están al principio de cada script.

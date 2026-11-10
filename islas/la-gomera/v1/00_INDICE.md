# La Gomera, despensa cerrada · v1 (10/11/2026) [BORRADOR]

Réplica para La Gomera del visor «La Palma, despensa cerrada» (territorio.visualizalapalma.es) con el pipeline multi-isla del repositorio (`pipeline/`). Generada con `pipeline/run.sh la-gomera`.

## Piezas firmables
- `01_RESUMEN.md` · resumen ejecutivo en cinco puntos · `04_lectura_balance.md` · escenarios y cifras · `03_catalogo_viabilidad.csv` · catálogo por pisos
- `05_visor_despensa_cerrada.html` · **el visor** (un solo HTML, sin red) · `aviso.html` · aviso, fuentes y licencias · `99_CARGA_PENDIENTE.html` · deuda y prompt de reinicio

## Soporte
- `90_verificacion.csv`, `90_test_resultado.json`, `cap_*.png` · pruebas · `91_fuentes_y_licencias.md` · fuentes F1–F12
- `mapa_oficial_resumen.json`, `92c_pisos_salida.json`, `95_catalogo_salida.json`, `97_balance_salida.json`, `94_territorio_salida.json`, `04b_cocina.json`, `tex_hoy.jpg`, `tex_fut.jpg` · salidas intermedias
- `parcelas.parquet` (no versionado) · parcelas con cota y pendiente; se regenera con `pipeline/00_preparar_parcelas.py la-gomera` a partir del shapefile en `_ref/shp/` y las teselas DEM en `_ref/dem/`

# Tenerife, despensa cerrada

Réplica para Tenerife del visor [«La Palma, despensa cerrada»](https://territorio.visualizalapalma.es/p/despensa-cerrada/) de Jorge Díaz Pérez y de su página de [carga pendiente](https://territorio.visualizalapalma.es/p/despensa-pendiente/). Prototipo divulgativo hecho con IA, sin carácter oficial.

Si el mundo se cerrara y la isla dejara de exportar plátano: qué se podría cultivar, criar y pescar, cuánta tierra y agua quedarían libres, qué habría en una nevera y una despensa solo con producto tinerfeño y, con 961.745 residentes, si alcanzaría (no: un 16 % en el escenario de referencia, un 38 % en el mejor caso).

## Estructura

- `v1/`, `v2/` · instantáneas completas de cada versión: visor (`05_visor_*.html`, un solo HTML sin red), carga pendiente (`99_CARGA_PENDIENTE_TF.html`), scripts (`93`, `96`, `93c`, `04b`, `98`, `99`), salidas, documentación (`00_INDICE.md`, `01_RESUMEN.md`, `04_lectura_balance_tf.md`, `91_fuentes_y_licencias_tf.md`, `90_verificacion_tf.csv`) y capturas de las pruebas. La vigente es la de número más alto.
- `pipeline/` · pipeline común para todas las islas (`run.sh <isla>`): parcelas con relieve, pisos climáticos de estaciones AEMET, catálogo ECOCROP, balance por programación lineal, mapa 3D, cocina, visor, carga pendiente y documentación. Parámetros por isla en `config_islas.json`; textos de cocina en `cocina_islas.json`.
- `islas/<isla>/vN/` · salidas congeladas de cada isla (Gran Canaria, Lanzarote, Fuerteventura, La Gomera, El Hierro). La Palma no se replica: existe el visor original de Jorge Díaz Pérez.
- `scripts/build_site.py` · monta `site/` con la estructura de URL de la web (`/p/despensa-cerrada/`, `/p/despensa-pendiente/`, `/aviso.html`, `/v1/`…`/v4/` de Tenerife y `/<isla>/` para las demás).
- `.github/workflows/deploy.yml` · en cada push a `main` monta `site/` y lo sube por FTP/FTPS o SFTP al hosting.

Los datos pesados (parcelas en GeoParquet, shapefiles del Mapa de Cultivos, teselas DEM, descargas de AEMET) van en `_ref/`, fuera del repositorio; cada `00_INDICE.md` dice de dónde descargarlos y cómo rehacer cada cifra.

## Publicación

En el repositorio, *Settings → Secrets and variables → Actions*:

| Tipo | Nombre | Valor |
|---|---|---|
| Secret | `FTP_SERVER` | host del hosting, p. ej. `ftp.midominio.es` |
| Secret | `FTP_USERNAME` | usuario FTP |
| Secret | `FTP_PASSWORD` | contraseña FTP |
| Variable | `FTP_REMOTE_DIR` | carpeta de destino relativa a la raíz del usuario FTP, con barra final; por defecto `./` (la raíz). Para una subcarpeta, p. ej. `./tenerife/` |
| Variable | `DEPLOY_PROTOCOL` | `ftps` (por defecto), `ftp` o `sftp` |
| Variable | `SFTP_PORT` | solo para SFTP, por defecto `22` |

El job `deploy` usa el *environment* `produccion`; créalo en *Settings → Environments* si quieres exigir aprobación manual antes de publicar. Sin él, basta con los secretos.

## Licencia

Código bajo [MIT](LICENSE); textos, ilustraciones y datos derivados bajo [CC BY 4.0](LICENSE-CONTENIDO.md), con atribución al visor original de La Palma y a los titulares de los datos. Detalle en `LICENSE-CONTENIDO.md`.

## Cómo contribuir

Se trabaja con git flow: `main` publica, `develop` integra, `feature/*`, `release/*` y `hotfix/*` para el trabajo. Detalle en `CONTRIBUTING.md`; las reglas para sesiones de IA están en `CLAUDE.md`.

## Fuentes

Mapa de Cultivos de Tenerife 2021 y registro de primera venta de pesca 2021 (Gobierno de Canarias, CC BY 4.0) · Copernicus DEM GLO-30 (ESA) · FAOSTAT y ECOCROP (FAO) · AEMET, normales 1991-2020 · ISTAC · Consejo Insular de Aguas de Tenerife. Detalle en `v2/91_fuentes_y_licencias_tf.md` y en `v2/aviso_tf.html`. Textos, ilustraciones y código propios, reutilizables citando la fuente; three.js (MIT) incrustado.

# Reglas del repositorio

## Git flow (obligatorio)
- `main` es producción: cada push a `main` publica la web por FTP (workflow «Publicar en la web»). Nunca se hace commit directo en `main`.
- `develop` es la rama de integración. Todo el trabajo sale de `develop` y vuelve a `develop`.
- Ramas de trabajo: `feature/<nombre-corto>` desde `develop`; se integran en `develop` con merge `--no-ff` (o pull request).
- Publicación: `release/vN.M` desde `develop`; `main` está protegida y solo admite cambios por pull request: se sube la rama, se abre un PR `release/vN.M` → `main`, se fusiona desde GitHub (merge commit, no squash), se crea la etiqueta `vN.M.P` en Releases y se fusiona `main` de vuelta a `develop`.
- Las etiquetas no se pueden subir desde esta sesión (el proxy las rechaza): se crean en GitHub → Releases.
- Urgencias en producción: `hotfix/<nombre>` desde `main`; se cierra con merge a `main` (y etiqueta) y a `develop`.
- Mensajes de commit en español, en imperativo o sentence case, con la primera línea de menos de 72 caracteres.
- Antes de abrir una release: `python3 scripts/build_site.py` debe terminar sin errores y las pruebas de `vN/90_test_visor.js` deben dar 0 externas, 0 errores y sin scroll horizontal.

## Versiones del visor
- Cada versión del visor vive en su carpeta congelada `vN/` (no se edita una versión cerrada; un cambio es `v(N+1)/`). La etiqueta `vN.M.P` de `main` corresponde a la carpeta `vN/` publicada en `/p/despensa-cerrada/`.
- Los datos pesados (`_dl/`, parquet, shapefiles, DEM) no se suben; cada `00_INDICE.md` dice cómo regenerarlos.

## Estilo del proyecto
- Léxico canario en textos visibles (papas, millo, batata o boniato); etiquetas epistémicas [VERIFICADO], [APROXIMADO], [INFERENCIA], [REQUIERE_FUENTE], [CONOCIMIENTO_BASE] en toda cifra.
- El visor es un único HTML sin red, con three.js incrustado.

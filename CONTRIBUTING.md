# Cómo se trabaja en este repositorio: git flow

| Rama | Para qué | Sale de | Vuelve a |
|---|---|---|---|
| `main` | producción; cada push publica la web | — | — |
| `develop` | integración de lo siguiente que se publicará | `main` (una vez) | — |
| `feature/<nombre>` | un cambio concreto (una escena, una fuente nueva, un script) | `develop` | `develop` |
| `release/vN.M` | preparar una publicación: números de versión, documentación, pruebas | `develop` | `main` y `develop` |
| `hotfix/<nombre>` | arreglar algo roto en producción | `main` | `main` y `develop` |

## Flujo habitual

```bash
git checkout develop && git pull
git checkout -b feature/clima-mar-de-nubes
# ... trabajo y commits ...
git checkout develop && git merge --no-ff feature/clima-mar-de-nubes && git push origin develop
git branch -d feature/clima-mar-de-nubes
```

## Publicar una versión

```bash
git checkout -b release/v3.0 develop
# ajustar documentación, 00_INDICE.md, pruebas
git push -u origin release/v3.0
gh pr create --base main --head release/v3.0 --title "Release v3.0" --body "..."
# main está protegida: se fusiona el PR desde GitHub con merge commit (no squash)
# después: crear la etiqueta v3.0.0 en GitHub → Releases, y
git checkout develop && git pull && git merge --no-ff main && git push origin develop
git branch -d release/v3.0
```

El push a `main` lanza el workflow «Publicar en la web» y la web se actualiza sola. El workflow «Comprobar montaje» se ejecuta en `develop`, en las ramas `feature/*`, `release/*` y `hotfix/*` y en los pull requests, y solo monta `site/` para comprobar que todo está en orden; no publica.

## Urgencias

```bash
git checkout -b hotfix/enlace-roto main
# ... arreglo ...
git checkout main && git merge --no-ff hotfix/enlace-roto && git tag -a v2.0.1 -m "v2.0.1" && git push origin main --tags
git checkout develop && git merge --no-ff hotfix/enlace-roto && git push origin develop
```

`main` está protegida en GitHub (regla: cambios solo por pull request), de modo que nadie, ni una sesión de IA, puede empujar directamente a producción. El check «Comprobar montaje» se ejecuta en el PR.

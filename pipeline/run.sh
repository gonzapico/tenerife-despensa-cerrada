#!/usr/bin/env bash
# Regenera una isla completa: pipeline/run.sh <isla>  (islas: ver config_islas.json). Requiere _ref/ (shapefiles, DEM, AEMET, plantilla de La Palma, ECOCROP).
set -euo pipefail
cd "$(dirname "$0")"; I="$1"
python3 00_preparar_parcelas.py "$I" && python3 92c_pisos.py "$I" >/dev/null && python3 93_catalogo.py "$I" | head -2 && python3 96_balance.py "$I" | grep -v '^    ' | sed -n 2p && python3 93c_territorio.py "$I" > "../islas/$I/${DESPENSA_VERSION:-v1}/93c_log.txt" 2>&1 && head -1 "../islas/$I/${DESPENSA_VERSION:-v1}/93c_log.txt" && python3 04b_cocina.py "$I" && python3 98_ensamblar.py "$I" && python3 99_carga_pendiente.py "$I"
OUT="../islas/$I/${DESPENSA_VERSION:-v1}"
node 90_test_visor.js "$OUT/05_visor_despensa_cerrada.html" > "$OUT/90_test_resultado.json" && mv -f cap_*.png "$OUT/" && node 90_test_pendiente.js "$OUT/99_CARGA_PENDIENTE.html" >/dev/null && rm -f cap_pend_*.png
python3 05_docs.py "$I"
python3 - "$OUT/90_test_resultado.json" <<'PY'
import json,sys; d=json.load(open(sys.argv[1])); v=d['vistas'][0]
print('TEST externas',d['externas'],'errores',d['errores'],'| scroll ok',all(x['scrollW']<=x['innerW'] for x in d['vistas']),'|',v['check1'][-10:],v['check4'][-10:],'|',v['calibra'])
PY

#!/usr/bin/env bash
#
# Generate Cinode TypeScript type definitions

SRC="https://api.cinode.com/swagger/v0.1/swagger.json"
DEST="$(pwd)/src/"
DEST_TS="$DEST/cinode.d.ts"
DEST_PY="$DEST/cinode-py-client"

python3 -m pip install --user --upgrade pipx
python3 -m pipx ensurepath
python3 -m pipx install openapi-python-client --include-deps

rm -rf "$DEST_PY"
openapi-python-client generate --url "$SRC"
mv "cinode-api-client" "$DEST_PY"

npx openapi-typescript \
  "$SRC" \
  --export-type \
  --path-params-as-type \
  --output "$DEST_TS"

npm run prettier


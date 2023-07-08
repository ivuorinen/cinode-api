#!/usr/bin/env bash
#
# Generate Cinode TypeScript type definitions

SRC="https://api.cinode.com/swagger/v0.1/swagger.json"
DEST="$(pwd)/src/cinode.d.ts"

npx openapi-typescript \
  "$SRC" \
  --export-type \
  --path-params-as-type \
  --output "$DEST"

npm run prettier


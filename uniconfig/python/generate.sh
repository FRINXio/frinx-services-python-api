#!/usr/bin/env bash

REST_API_PATH='frinx_api/uniconfig/rest_api.py'

# remove obsolete files, because are not cleaned during generations
API_PATH='frinx_api/uniconfig/'

uid=$(stat -c '%u' ${API_PATH} )
gid=$(stat -c '%g' ${API_PATH} )

rm -rf frinx_api/uniconfig/*

poetry install

poetry run datamodel-codegen \
  --disable-timestamp \
  --use-field-description \
  --use-schema-description \
  --use-default \
  --field-constraints \
  --collapse-root-models \
  --use-standard-collections \
  --allow-population-by-field-name \
  --input /swagger/uniconfig.yaml \
  --input-file-type openapi \
  --openapi-scopes paths \
  --output frinx_api/uniconfig \
  --output-model-type pydantic_v2.BaseModel \
  --target-python-version 3.10 \
  --custom-file-header "# generated by datamodel-codegen"

# generate rest_api file to map URL, Method and models from datamodel-codegen
poetry run python3 ./generate_rest_api.py --input /swagger/uniconfig.yaml --output ${REST_API_PATH}

# apply patches
cat ./patches/rest_api.txt >> ${REST_API_PATH}

## use default formatting
poetry run ruff --fix . || true

chown -R "${uid}:${gid}" frinx_api/uniconfig/*

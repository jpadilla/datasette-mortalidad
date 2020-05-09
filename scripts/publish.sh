#!/bin/bash

echo "=> publishing..."
datasette publish heroku \
  -n datasette-mortalidad \
  -m ./metadata.json \
  --extra-options="--config default_cache_ttl:3600 --config hash_urls:1" \
  ./assets/mortalidad.db

#!/bin/bash

echo "=> starting..."
datasette serve \
  -m ./metadata.json \
  -i ./assets/mortalidad.db

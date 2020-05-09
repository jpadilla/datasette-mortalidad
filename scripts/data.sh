#!/bin/bash

echo "=> downloading from dropbox..."
curl -Ls -o ./assets/source.zip https://www.dropbox.com/sh/81jpdrwuq2wwscg/AACXHw03QEVncrWG6urKLGZca?dl=1

echo "=> extracting assets..."
(cd ./assets && unzip -o source.zip)

echo "=> converting xlsx to csv..."
xlsx2csv ./assets/2007-2014.xlsx ./assets/original-2007-2014.csv
xlsx2csv ./assets/2015-2020.xlsx ./assets/original-2015-2020.csv

echo "=> preprocessing csvs..."
python ./scripts/preprocess_csv.py

echo "=> converting csv to sqlite..."
csvs-to-sqlite ./assets/2007-2014.csv ./assets/2015-2020.csv ./assets/mortalidad.db

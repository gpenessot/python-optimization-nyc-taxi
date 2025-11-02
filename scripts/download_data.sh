#!/bin/bash

# Script pour télécharger le dataset NYC Yellow Taxi

echo "📥 Téléchargement du dataset NYC Yellow Taxi (Janvier 2022)..."
echo "Source: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"

# URL du fichier Parquet
URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet"
OUTPUT="data/yellow_taxi.parquet"

# Téléchargement avec curl ou wget
if command -v curl &> /dev/null; then
    curl -L "$URL" -o "$OUTPUT"
elif command -v wget &> /dev/null; then
    wget "$URL" -O "$OUTPUT"
else
    echo "❌ Erreur: curl ou wget requis pour télécharger les données"
    exit 1
fi

echo "✅ Dataset téléchargé: $OUTPUT"
echo "📊 Taille: $(du -h $OUTPUT | cut -f1)"

#!/bin/bash

# Script d'aide pour exécuter les différentes parties du projet

case "$1" in
    setup)
        echo "🔧 Installation des dépendances..."
        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        echo "✅ Setup terminé"
        ;;
    download)
        echo "📥 Téléchargement des données..."
        bash scripts/download_data.sh
        ;;
    profile)
        echo "🔬 Profiling avec py-spy..."
        py-spy record -o results/profile.svg -- python src/01_profiling.py
        echo "📊 Flamegraph généré: results/profile.svg"
        ;;
    benchmark)
        echo "🚀 Exécution des benchmarks..."
        python benchmarks/run_all_benchmarks.py
        ;;
    *)
        echo "Usage: ./run.sh {setup|download|profile|benchmark}"
        echo ""
        echo "Commandes disponibles:"
        echo "  setup      - Créer l'environnement et installer les dépendances"
        echo "  download   - Télécharger le dataset NYC Taxi"
        echo "  profile    - Profiler le script avec py-spy"
        echo "  benchmark  - Exécuter tous les benchmarks"
        exit 1
        ;;
esac

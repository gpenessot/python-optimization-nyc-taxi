# Guide de démarrage rapide

## Installation (5 minutes)
```bash
# 1. Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Télécharger le dataset
bash scripts/download_data.sh
```

## Utilisation rapide

### Avec le script d'aide
```bash
./run.sh setup      # Installation
./run.sh download   # Télécharger les données
./run.sh profile    # Profiler avec py-spy
./run.sh benchmark  # Tous les benchmarks
```

### Manuellement
```bash
# Profiling
py-spy record -o results/profile.svg -- python src/01_profiling.py

# Benchmark individuel
python src/02_loading.py

# Tous les benchmarks
python benchmarks/run_all_benchmarks.py
```

## Résultats attendus

- **DuckDB vs Pandas** : 4-5x plus rapide
- **Vectorisation** : 100-500x plus rapide
- **Parallélisation** : 4-8x plus rapide
- **Caching** : 10-50x plus rapide

## Ressources

- [Newsletter DataGyver](https://datagy.substack.com/)
- [py-spy Documentation](https://github.com/benfred/py-spy)
- [DuckDB Documentation](https://duckdb.org/docs/)

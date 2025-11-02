# Python Optimization - NYC Taxi Dataset

> De 2h17 à 11 minutes : Comment optimiser vos scripts Python
> Newsletter DataGyver #9

## 🎯 Objectif

Ce projet démontre 3 techniques d'optimisation Python mesurables et reproductibles :

1. **Profiling avec py-spy** - Identifier les goulots d'étranglement
2. **Lazy Loading avec DuckDB** - Charger uniquement ce qui est nécessaire
3. **Vectorisation** - Éliminer les boucles Python lentes

## 📊 Dataset

NYC Yellow Taxi Trip Records (Janvier 2022)
- 2.4M trajets
- ~38 Mo au format Parquet
- Source : [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

## 🚀 Installation
```bash
# Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sur Windows

# Installer les dépendances
pip install -r requirements.txt
```

## 📁 Structure du projet
```
.
├── src/
│   ├── utils/                 # Utilitaires communs
│   ├── 01_profiling.py        # Démonstration py-spy
│   ├── 02_loading.py          # Pandas vs DuckDB
│   ├── 03_vectorization.py    # Boucles vs vectorisation
│   ├── 04_parallelization.py  # Traitement parallèle
│   ├── 05_caching.py          # LRU cache
│   └── 06_full_benchmark.py   # Benchmark complet
├── benchmarks/
│   └── run_all_benchmarks.py  # Exécute tous les benchmarks
├── scripts/
│   └── download_data.sh       # Télécharge le dataset NYC Taxi
├── data/                      # Données (gitignored)
├── results/                   # Résultats des benchmarks
└── docs/                      # Documentation
```

## 🔬 Utilisation

### 1. Profiling avec py-spy
```bash
# Exécuter le script et générer le flamegraph
py-spy record -o results/profile.svg -- python src/01_profiling.py

# Ouvrir le flamegraph dans votre navigateur
open results/profile.svg  # macOS
xdg-open results/profile.svg  # Linux
start results/profile.svg  # Windows
```

### 2. Benchmark Pandas vs DuckDB
```bash
python src/02_loading.py
```

### 3. Vectorisation
```bash
python src/03_vectorization.py
```

### 4. Tous les benchmarks
```bash
python benchmarks/run_all_benchmarks.py
```

## 📈 Résultats attendus

| Technique | Gain mesuré | Impact |
|-----------|-------------|--------|
| DuckDB vs Pandas | 4-5x | Chargement & agrégation |
| Vectorisation | 100-500x | Calculs sur colonnes |
| Parallélisation | 4-8x | Traitement multi-fichiers |
| Caching | 10-50x | Appels répétitifs |

## 🎓 Pour aller plus loin

- [Newsletter DataGyver](https://datagy.substack.com/)
- [Formation Streamlit Unleashed](lien)
- [SQL Mastery](lien)

## 📝 Licence

MIT - Gaël Penessot

---

**💡 Contribuez :** Partagez vos propres optimisations en créant une issue ou PR !

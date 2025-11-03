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

### Prérequis
- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (gestionnaire de packages ultra-rapide)

### Installation rapide avec uv (recommandé)
```bash
# Installer uv si nécessaire
# Windows: pip install uv
# macOS/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh

# Créer l'environnement virtuel
uv venv

# Activer l'environnement
# Windows PowerShell:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Installer les dépendances (rapide avec uv!)
uv pip install -r requirements.txt

# Télécharger le dataset NYC Taxi (~38 Mo)
curl -L "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet" -o "data/yellow_taxi.parquet"
# Ou sur Windows avec PowerShell:
# Invoke-WebRequest -Uri "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet" -OutFile "data/yellow_taxi.parquet"
```

### Installation avec pip (alternative)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
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

### Exécution rapide avec uv
```bash
# 1. Profiling - Identifier les goulots d'étranglement
uv run src/01_profiling.py

# 2. Benchmark Pandas vs DuckDB - Lazy loading
uv run src/02_loading.py

# 3. Vectorisation - Boucles vs opérations vectorisées
uv run src/03_vectorization.py

# 4. Parallélisation - Traitement multi-fichiers
uv run src/04_parallelization.py

# 5. Caching LRU - Mémoisation des résultats
uv run src/05_caching.py

# 6. Benchmark complet - Tous les tests
uv run benchmarks/run_all_benchmarks.py
```

### Profiling avancé avec py-spy (nécessite droits admin sur Windows)
```bash
# Générer un flamegraph interactif
py-spy record -o results/profile.svg -- python src/01_profiling.py

# Ouvrir le flamegraph dans votre navigateur
start results/profile.svg  # Windows
open results/profile.svg   # macOS
xdg-open results/profile.svg  # Linux
```

**Note :** Sur Windows, py-spy nécessite des droits administrateur. Lancez PowerShell en tant qu'administrateur si vous obtenez une erreur de permissions.

## 📈 Résultats mesurés

Résultats obtenus sur Windows 11, Python 3.12, CPU Intel/AMD moderne :

| Technique | Gain mesuré | Temps avant | Temps après | Impact |
|-----------|-------------|-------------|-------------|--------|
| **DuckDB vs Pandas** | **8.6x plus rapide** | 4.4s | 0.5s | Chargement & agrégation |
| **Vectorisation** | **1,821x plus rapide** | 135s | 0.07s | Calculs sur colonnes |
| **Caching LRU** | **3,350x plus rapide** | 78s | 0.02s | Appels répétitifs |
| **Profiling py-spy** | Boucle = 99.7% du temps | - | - | Identification du goulot |

### ⚠️ Note sur la parallélisation
La parallélisation n'est efficace que sur des **traitements lourds** (fichiers >10 Mo ou calculs intensifs). Sur de petits fichiers, l'overhead de création de processus peut annuler le gain. Toujours profiler avant de paralléliser !

### 💡 Leçon clé
**Le vrai goulot d'étranglement :** Les boucles `for` sur DataFrames représentent 99.7% du temps d'exécution dans le script non optimisé. La vectorisation offre les gains les plus spectaculaires (1,821x).

## 🧪 Vérifier que tout fonctionne

Pour tester rapidement l'installation :

```bash
# Test rapide : Benchmark complet (environ 3-4 minutes)
uv run benchmarks/run_all_benchmarks.py

# Vérifier un script spécifique
uv run src/02_loading.py
```

Si vous voyez des résultats de performances s'afficher, tout fonctionne correctement ! 🎉

## 📚 Détails des scripts

- **`01_profiling.py`** : Démontre l'utilisation de py-spy pour identifier où le code perd son temps (boucle for vs merge)
- **`02_loading.py`** : Compare Pandas et DuckDB pour le chargement et l'agrégation de données
- **`03_vectorization.py`** : Montre la différence massive entre boucles for et opérations vectorisées
- **`04_parallelization.py`** : Démontre la parallélisation (avec avertissement sur les petits fichiers)
- **`05_caching.py`** : Illustre l'impact du caching LRU sur les appels répétitifs
- **`06_full_benchmark.py`** : Compare Pandas, Polars et DuckDB sur plusieurs opérations

## 🎓 Pour aller plus loin

**Newsletter & Formations :**
- [Newsletter DataGyver](https://datagy.substack.com/) - Techniques data chaque semaine
- Formation Streamlit Unleashed - Construire des apps data performantes
- SQL Mastery - Optimisation SQL et bases de données

**Ressources techniques :**
- [py-spy Documentation](https://github.com/benfred/py-spy)
- [DuckDB Performance Guide](https://duckdb.org/why_duckdb)
- [Polars User Guide](https://docs.pola.rs/)

## 🤝 Contribuer

Vous avez optimisé un script avec ces techniques ? Partagez vos résultats !

1. Fork le repo
2. Ajoutez votre exemple dans un nouveau script
3. Créez une Pull Request avec vos résultats

Ou simplement ouvrez une issue pour partager votre histoire d'optimisation !

## 📝 Licence

MIT - Gaël Penessot

---

**💡 Ce projet est 100% transparent :** Tous les chiffres annoncés sont reproductibles. Clone le repo et vérifie par toi-même !

"""
Exécute tous les benchmarks et génère un rapport
"""

import subprocess
import sys
from pathlib import Path

BENCHMARKS = [
    ('01_profiling.py', 'Profiling avec py-spy'),
    ('02_loading.py', 'Pandas vs DuckDB'),
    ('03_vectorization.py', 'Vectorisation vs Boucles'),
    ('04_parallelization.py', 'Traitement parallèle'),
    ('05_caching.py', 'Caching LRU'),
    ('06_full_benchmark.py', 'Benchmark complet'),
]

def run_benchmark(script_name: str, description: str):
    """Exécute un script de benchmark"""
    print(f"\n{'='*60}")
    print(f"🔬 {description}")
    print(f"{'='*60}")
    
    script_path = Path('src') / script_name
    result = subprocess.run([sys.executable, str(script_path)])
    
    return result.returncode == 0

def main():
    print("🚀 EXÉCUTION DE TOUS LES BENCHMARKS")
    print("Newsletter DataGyver #9 - Optimisation Python")
    
    results = {}
    for script, desc in BENCHMARKS:
        success = run_benchmark(script, desc)
        results[script] = success
    
    # Résumé
    print(f"\n{'='*60}")
    print("📊 RÉSUMÉ")
    print(f"{'='*60}")
    
    for script, success in results.items():
        status = "✅" if success else "❌"
        print(f"{status} {script}")
    
    total = len(results)
    passed = sum(results.values())
    print(f"\n{passed}/{total} benchmarks réussis")

if __name__ == "__main__":
    main()

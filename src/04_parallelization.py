"""
Démonstration : Traitement parallèle de plusieurs fichiers
Newsletter DataGyver #9 - Optimisation Python
"""

import time
import pandas as pd
import numpy as np
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

def process_file(filepath: str) -> dict:
    """Traite un fichier CSV et retourne des statistiques"""
    df = pd.read_csv(filepath)
    
    return {
        'file': Path(filepath).name,
        'rows': len(df),
        'total_revenue': df['revenue'].sum(),
        'avg_revenue': df['revenue'].mean()
    }

def create_sample_files(n_files: int = 12, rows_per_file: int = 50_000):
    """Crée des fichiers CSV d'exemple pour le benchmark"""
    print(f"Création de {n_files} fichiers de test...")
    
    output_dir = Path('sample_data')
    output_dir.mkdir(exist_ok=True)
    
    files = []
    for i in range(n_files):
        filepath = output_dir / f'sales_{i:02d}.csv'
        df = pd.DataFrame({
            'customer_id': np.random.randint(1000, 9999, rows_per_file),
            'revenue': np.random.uniform(100, 5000, rows_per_file),
            'date': pd.date_range('2024-01-01', periods=rows_per_file, freq='1h')
        })
        df.to_csv(filepath, index=False)
        files.append(str(filepath))
    
    print(f"✅ Fichiers créés dans {output_dir}/")
    return files

def sequential_processing(files: list) -> tuple:
    """Traitement séquentiel (1 fichier à la fois)"""
    print("\n🐌 Traitement SÉQUENTIEL")
    start = time.time()
    
    results = [process_file(f) for f in files]
    
    elapsed = time.time() - start
    print(f"Temps: {elapsed:.2f}s")
    return results, elapsed

def parallel_processing(files: list, max_workers: int = None) -> tuple:
    """Traitement parallèle (plusieurs fichiers simultanément)"""
    print(f"\n⚡ Traitement PARALLÈLE ({max_workers or 'auto'} workers)")
    start = time.time()
    
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(process_file, files))
    
    elapsed = time.time() - start
    print(f"Temps: {elapsed:.2f}s")
    return results, elapsed

def main():
    print("Démonstration : Traitement parallèle de fichiers")
    print("=" * 60)
    
    # Création des fichiers de test
    files = create_sample_files(n_files=12, rows_per_file=50_000)
    
    # Traitement séquentiel
    _, seq_time = sequential_processing(files)
    
    # Traitement parallèle
    _, par_time = parallel_processing(files, max_workers=4)
    
    # Comparaison
    print("\n" + "=" * 60)
    print("RÉSULTATS")
    print("=" * 60)
    speedup = seq_time / par_time
    print(f"Le traitement parallèle est {speedup:.1f}x plus rapide")
    print(f"Temps économisé: {seq_time - par_time:.2f}s ({(1-par_time/seq_time)*100:.1f}%)")

if __name__ == "__main__":
    main()

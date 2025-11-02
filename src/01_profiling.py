"""
Script de démonstration pour profiler un code Python avec py-spy
Newsletter DataGyver #9 - Optimisation Python
"""

import time
import pandas as pd
import numpy as np

def slow_data_processing():
    """Exemple de traitement de données non optimisé"""
    # Génération de données de test
    n_rows = 100_000
    df = pd.DataFrame({
        'customer_id': np.random.randint(1000, 9999, n_rows),
        'product_id': np.random.randint(100, 999, n_rows),
        'revenue': np.random.uniform(10, 1000, n_rows),
        'date': pd.date_range('2024-01-01', periods=n_rows, freq='1min'),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n_rows)
    })
    
    # Opération coûteuse : merge
    df2 = pd.DataFrame({
        'customer_id': np.arange(1000, 10000),
        'customer_name': [f'Customer_{i}' for i in range(1000, 10000)]
    })
    
    print("Début du merge...")
    start = time.time()
    result = df.merge(df2, on='customer_id', how='left')
    print(f"Merge terminé en {time.time()-start:.2f}s")
    
    # Boucle inefficace sur les lignes
    print("Début de la boucle...")
    start = time.time()
    for i in range(len(result)):
        result.loc[i, 'margin'] = result.loc[i, 'revenue'] * 0.3
    print(f"Boucle terminée en {time.time()-start:.2f}s")
    
    return result

if __name__ == "__main__":
    print("Exécution du script lent...")
    print("Pour profiler: py-spy record -o profile.svg -- python src/01_profiling.py")
    df = slow_data_processing()
    print(f"Traitement terminé. {len(df)} lignes traitées.")

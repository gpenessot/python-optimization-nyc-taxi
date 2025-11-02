"""
Démonstration : Vectorisation vs Boucles for
Newsletter DataGyver #9 - Optimisation Python
"""

import time
import pandas as pd
import numpy as np

def with_loop(df: pd.DataFrame) -> tuple:
    """Calcul avec boucle for (LENT)"""
    start = time.time()
    
    for i in range(len(df)):
        df.loc[i, 'margin'] = df.loc[i, 'revenue'] * 0.3
        df.loc[i, 'discount'] = df.loc[i, 'revenue'] * 0.1
        df.loc[i, 'net_revenue'] = df.loc[i, 'revenue'] - df.loc[i, 'discount']
    
    elapsed = time.time() - start
    return df, elapsed

def with_vectorization(df: pd.DataFrame) -> tuple:
    """Calcul vectorisé (RAPIDE)"""
    start = time.time()
    
    df['margin'] = df['revenue'] * 0.3
    df['discount'] = df['revenue'] * 0.1
    df['net_revenue'] = df['revenue'] - df['discount']
    
    elapsed = time.time() - start
    return df, elapsed

def main():
    print("Démonstration : Vectorisation vs Boucles")
    print("=" * 60)
    
    # Génération de données de test
    n_rows = 100_000
    print(f"\nGénération de {n_rows:,} lignes...")
    
    df_base = pd.DataFrame({
        'customer_id': np.random.randint(1000, 9999, n_rows),
        'revenue': np.random.uniform(100, 5000, n_rows)
    })
    
    # Test avec boucle
    print("\n🐌 Test avec boucle for...")
    df_loop = df_base.copy()
    _, loop_time = with_loop(df_loop)
    print(f"Temps: {loop_time:.2f}s")
    
    # Test vectorisé
    print("\n⚡ Test avec vectorisation...")
    df_vec = df_base.copy()
    _, vec_time = with_vectorization(df_vec)
    print(f"Temps: {vec_time:.2f}s")
    
    # Comparaison
    print("\n" + "=" * 60)
    print("RÉSULTATS")
    print("=" * 60)
    speedup = loop_time / vec_time
    print(f"La vectorisation est {speedup:.0f}x plus rapide")
    print(f"Temps économisé: {loop_time - vec_time:.2f}s ({(1-vec_time/loop_time)*100:.1f}%)")
    
    # Vérification
    assert abs(df_loop['margin'].sum() - df_vec['margin'].sum()) < 0.01, "Résultats différents!"
    print("\n✅ Résultats identiques vérifiés")

if __name__ == "__main__":
    main()

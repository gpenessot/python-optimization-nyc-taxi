"""
Benchmark : Pandas vs DuckDB pour chargement et agrégation
Newsletter DataGyver #9 - Optimisation Python
"""

import time
import pandas as pd
import duckdb

def benchmark_pandas(filepath: str):
    """Charge et agrège avec Pandas"""
    print("\n=== PANDAS ===")
    
    # Chargement
    start = time.time()
    df = pd.read_parquet(filepath)
    load_time = time.time() - start
    print(f"Lecture: {load_time:.2f}s")
    
    # Agrégation
    start = time.time()
    df['pickup_date'] = pd.to_datetime(df['tpep_pickup_datetime']).dt.date
    result = df.groupby('pickup_date')['total_amount'].agg(['sum', 'mean', 'count'])
    agg_time = time.time() - start
    print(f"Agrégation: {agg_time:.2f}s")
    print(f"Total: {load_time + agg_time:.2f}s")
    
    return result, load_time + agg_time

def benchmark_duckdb(filepath: str):
    """Charge et agrège avec DuckDB"""
    print("\n=== DUCKDB ===")
    
    start = time.time()
    result = duckdb.sql(f"""
        SELECT 
            DATE_TRUNC('day', tpep_pickup_datetime) AS pickup_date,
            SUM(total_amount) AS total_sum,
            AVG(total_amount) AS avg_amount,
            COUNT(*) AS trip_count
        FROM '{filepath}'
        GROUP BY pickup_date
    """).df()
    total_time = time.time() - start
    
    print(f"Lecture + agrégation: {total_time:.2f}s")
    
    return result, total_time

def main():
    # Chemin vers le fichier NYC Yellow Taxi
    filepath = 'data/yellow_taxi.parquet'
    
    print("Benchmark Pandas vs DuckDB sur NYC Yellow Taxi dataset")
    print("=" * 60)
    
    try:
        # Test Pandas
        _, pandas_time = benchmark_pandas(filepath)
        
        # Test DuckDB
        _, duckdb_time = benchmark_duckdb(filepath)
        
        # Comparaison
        print("\n" + "=" * 60)
        print("RÉSULTATS")
        print("=" * 60)
        speedup = pandas_time / duckdb_time
        print(f"DuckDB est {speedup:.1f}x plus rapide que Pandas")
        print(f"Gain de temps: {pandas_time - duckdb_time:.2f}s ({(1-duckdb_time/pandas_time)*100:.1f}%)")
    
    except FileNotFoundError:
        print(f"\n❌ Fichier {filepath} non trouvé")
        print("Exécutez: bash scripts/download_data.sh")

if __name__ == "__main__":
    main()

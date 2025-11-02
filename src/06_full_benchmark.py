"""
Benchmark complet : Toutes les techniques d'optimisation
Newsletter DataGyver #9 - Optimisation Python
"""

import time
import pandas as pd
import polars as pl
import duckdb
import numpy as np
from pathlib import Path

class PerformanceBenchmark:
    """Classe pour benchmarker différentes approches d'optimisation"""
    
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
        self.results = {}
    
    def benchmark_loading(self):
        """Compare les méthodes de chargement"""
        print("\n" + "="*60)
        print("BENCHMARK 1: CHARGEMENT DES DONNÉES")
        print("="*60)
        
        # Pandas
        start = time.time()
        df_pandas = pd.read_parquet(self.data_path)
        pandas_time = time.time() - start
        print(f"Pandas: {pandas_time:.3f}s")
        
        # Polars
        start = time.time()
        df_polars = pl.read_parquet(self.data_path)
        polars_time = time.time() - start
        print(f"Polars: {polars_time:.3f}s")
        
        # DuckDB
        start = time.time()
        df_duckdb = duckdb.sql(f"SELECT * FROM '{self.data_path}'").df()
        duckdb_time = time.time() - start
        print(f"DuckDB: {duckdb_time:.3f}s")
        
        self.results['loading'] = {
            'pandas': pandas_time,
            'polars': polars_time,
            'duckdb': duckdb_time
        }
        
        return df_pandas, df_polars
    
    def benchmark_aggregation(self, df_pandas: pd.DataFrame):
        """Compare les agrégations"""
        print("\n" + "="*60)
        print("BENCHMARK 2: AGRÉGATIONS")
        print("="*60)
        
        # Pandas avec boucle (pire approche)
        df_loop = df_pandas.copy()
        start = time.time()
        for i in range(min(1000, len(df_loop))):
            df_loop.loc[i, 'test'] = df_loop.loc[i, 'total_amount'] * 0.3
        loop_time = time.time() - start
        print(f"Pandas avec boucle (1000 lignes): {loop_time:.3f}s")
        
        # Pandas vectorisé
        start = time.time()
        df_pandas['test'] = df_pandas['total_amount'] * 0.3
        vectorized_time = time.time() - start
        print(f"Pandas vectorisé: {vectorized_time:.3f}s")
        
        # DuckDB
        start = time.time()
        result = duckdb.sql(f"""
            SELECT 
                DATE_TRUNC('day', tpep_pickup_datetime) as date,
                SUM(total_amount) as total,
                AVG(total_amount) as avg
            FROM '{self.data_path}'
            GROUP BY date
        """).df()
        duckdb_time = time.time() - start
        print(f"DuckDB agrégation: {duckdb_time:.3f}s")
        
        self.results['aggregation'] = {
            'loop': loop_time,
            'vectorized': vectorized_time,
            'duckdb': duckdb_time
        }
    
    def print_summary(self):
        """Affiche un résumé des résultats"""
        print("\n" + "="*60)
        print("RÉSUMÉ DES GAINS")
        print("="*60)
        
        # Chargement
        if 'loading' in self.results:
            fastest_load = min(self.results['loading'].values())
            slowest_load = max(self.results['loading'].values())
            print(f"\n📥 Chargement: {slowest_load/fastest_load:.1f}x de différence")
            for method, time_val in self.results['loading'].items():
                speedup = slowest_load / time_val
                print(f"  {method:10s}: {time_val:.3f}s (×{speedup:.1f})")
        
        # Agrégation
        if 'aggregation' in self.results:
            fastest_agg = min(self.results['aggregation'].values())
            slowest_agg = max(self.results['aggregation'].values())
            print(f"\n🔄 Agrégation: {slowest_agg/fastest_agg:.1f}x de différence")
            for method, time_val in self.results['aggregation'].items():
                speedup = slowest_agg / time_val
                print(f"  {method:10s}: {time_val:.3f}s (×{speedup:.1f})")

def main():
    data_path = "data/yellow_taxi.parquet"
    
    if not Path(data_path).exists():
        print(f"❌ Fichier {data_path} non trouvé")
        print("Exécutez: bash scripts/download_data.sh")
        return
    
    print("🚀 BENCHMARK COMPLET D'OPTIMISATION PYTHON")
    print("Newsletter DataGyver #9")
    
    benchmark = PerformanceBenchmark(data_path)
    
    # Exécution des benchmarks
    df_pandas, df_polars = benchmark.benchmark_loading()
    benchmark.benchmark_aggregation(df_pandas)
    
    # Résumé
    benchmark.print_summary()
    
    print("\n✅ Benchmark terminé!")
    print("\nPour profiler ce script avec py-spy:")
    print("py-spy record -o profile.svg -- python src/06_full_benchmark.py")

if __name__ == "__main__":
    main()

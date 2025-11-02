"""
Démonstration : Mise en cache pour éviter les calculs répétés
Newsletter DataGyver #9 - Optimisation Python
"""

import time
import random
from functools import lru_cache

# Simulation d'un mapping pays -> code ISO
COUNTRY_CODES = {
    'France': 'FR',
    'Germany': 'DE',
    'Spain': 'ES',
    'Italy': 'IT',
    'United Kingdom': 'GB',
    'Belgium': 'BE',
    'Netherlands': 'NL',
    'Switzerland': 'CH',
    'Austria': 'AT',
    'Portugal': 'PT'
}

def get_country_code_no_cache(country_name: str) -> str:
    """Recherche sans cache (simule un appel coûteux)"""
    time.sleep(0.001)  # Simule une recherche coûteuse
    return COUNTRY_CODES.get(country_name, 'XX')

@lru_cache(maxsize=None)
def get_country_code_cached(country_name: str) -> str:
    """Recherche avec cache LRU"""
    time.sleep(0.001)  # Simule une recherche coûteuse
    return COUNTRY_CODES.get(country_name, 'XX')

def main():
    print("Démonstration : Caching avec lru_cache")
    print("=" * 60)
    
    # Génération de 50K appels avec répétitions
    n_calls = 50_000
    countries = list(COUNTRY_CODES.keys())
    calls = [random.choice(countries) for _ in range(n_calls)]
    
    unique_countries = len(set(calls))
    print(f"\n{n_calls:,} appels de fonction")
    print(f"{unique_countries} valeurs uniques (beaucoup de répétitions)")
    
    # Test sans cache
    print("\n🐌 Sans cache...")
    start = time.time()
    results_no_cache = [get_country_code_no_cache(c) for c in calls]
    time_no_cache = time.time() - start
    print(f"Temps: {time_no_cache:.2f}s")
    
    # Test avec cache
    print("\n⚡ Avec cache LRU...")
    start = time.time()
    results_cached = [get_country_code_cached(c) for c in calls]
    time_cached = time.time() - start
    print(f"Temps: {time_cached:.2f}s")
    
    # Statistiques du cache
    cache_info = get_country_code_cached.cache_info()
    print(f"\nStatistiques cache:")
    print(f"  Hits: {cache_info.hits:,}")
    print(f"  Misses: {cache_info.misses:,}")
    print(f"  Taux de hit: {cache_info.hits/(cache_info.hits+cache_info.misses)*100:.1f}%")
    
    # Comparaison
    print("\n" + "=" * 60)
    print("RÉSULTATS")
    print("=" * 60)
    speedup = time_no_cache / time_cached
    print(f"Le cache est {speedup:.0f}x plus rapide")
    print(f"Temps économisé: {time_no_cache - time_cached:.2f}s ({(1-time_cached/time_no_cache)*100:.1f}%)")
    
    # Vérification
    assert results_no_cache == results_cached, "Résultats différents!"
    print("\n✅ Résultats identiques vérifiés")

if __name__ == "__main__":
    main()

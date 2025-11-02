"""
Utilitaires communs pour les benchmarks
"""

import time
from functools import wraps

def timeit(func):
    """Décorateur pour mesurer le temps d'exécution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} terminé en {elapsed:.3f}s")
        return result
    return wrapper

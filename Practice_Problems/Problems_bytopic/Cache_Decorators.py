'''
**Problem 2 — Cache Decorator**
```
Create a decorator that caches the results
of a function so it doesn't recompute
the same input twice.

@cache
def expensive_calculation(n):
    return n * n

expensive_calculation(5)  # computes → 25
expensive_calculation(5)  # returns from cache → 25
expensive_calculation(6)  # computes → 36
```
'''
from functools import wraps 

def Cache_Memory(func):
    memory = {}              # cache dictionary
    
    @wraps(func)
    def wrapper(*args):      # accepts any arguments
        if args in memory:   # check cache first
            print(f"From cache: {memory[args]}")
        else:
            result = func(*args)      # compute result
            memory[args] = result     # store in cache
            print(f"Computed: {result}")
    return wrapper           

@Cache_Memory
def expensive_calculation(n):
    return n * n

expensive_calculation(5)
expensive_calculation(5)
expensive_calculation(6)
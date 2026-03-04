'''
**Problem 3 — Validate Input Decorator**
```
Create a decorator that validates all
arguments of a function are positive numbers.
If not → raise ValueError.

@validate_positive
def calculate_area(length, width):
    return length * width

calculate_area(5, 3)   # ✅ 15
calculate_area(-1, 3)  # ❌ ValueError: "All arguments must be positive!"
```

'''
import functools
def validate_positive(func):

    @functools.wraps(func)
    def wrapper(*args):
        for arg in args:
            if arg<=0:
                raise ValueError("All arguments must be positive and greater than 0!")
            else:   
                result = func(*args)
                print(result)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width 

calculate_area(5, 3)      
calculate_area(-5, 3)        

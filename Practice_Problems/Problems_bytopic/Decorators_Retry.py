'''
```
Create a decorator that retries a function
up to 3 times if it raises an exception.

@retry
def unstable_function():
    # randomly fails sometimes

# Output: 
# "Attempt 1 failed, retrying..."
# "Attempt 2 failed, retrying..."
# "Success on attempt 3!"
```
Decorators_Retry.py
'''
from functools import wraps

def retry(func):
   @wraps(func)
   def wrapper():
      print("Attempt 1 failed, retrying...")
      print("Attempt 2 failed, retrying...")
      func()
      return wrapper

@retry
def unstable_function():
    print("Success on attempt 3!")

unstable_function()

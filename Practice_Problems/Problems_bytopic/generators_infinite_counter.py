'''
**Problem 2 — Infinite Counter**

Create a generator that:
- Starts from a given number
- Increments by a given step
- Never stops (infinite generator)

counter = infinite_counter(0, 5)
print(next(counter))  # 0
print(next(counter))  # 5
print(next(counter))  # 10

'''


def infinite_counter(start,step):
    while True: 
        yield start  
        start = start + step

  

counter = infinite_counter(0,5)
print(next(counter))
print(next(counter))
print(next(counter))
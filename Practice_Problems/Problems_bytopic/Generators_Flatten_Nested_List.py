'''
**Problem 3 — Flatten Nested List Generator**
```
Create a generator that yields items
from a deeply nested list one by one.

gen = flatten_generator([1, [2, [3, 4]], [5, 6]])
Output: 1, 2, 3, 4, 5, 6
```
'''

def flatten_list_generator(lst):
    for item in lst:
        if isinstance(item,list):
            yield from flatten_list_generator(item)
        else:
            yield item
            

gen = flatten_list_generator([1, [2, [3, 4]], [5, 6]])

print([x for x in gen])

    

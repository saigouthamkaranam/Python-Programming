'''
Practice Problem: Write a function that merges two dictionaries. 
If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.
'''

# My Approach:

# dict_A = {'a': 10, 'b': 20} 
# dict_b = {'b': 5, 'c': 15}

# Merged_Dictionary = {}

# for (x,y) in dict_b.items():
#     if x in dict_A.keys():
#         z = dict_A.get(x)
#         y = y+z
#     else:
#         pass
#     dict_A[x] = y

# print(dict_A)


'''
WHY THIS THIS IS NOT EFFICIENT
- Modifies the original dict_A directly — this is a side effect. If you need dict_A later in your program, it's already changed.
- else: pass is completely unnecessary noise.
- x in dict_A.keys() works but is redundant — x in dict_A is simpler and more Pythonic.
- Creates no reusable function, so it's not portable.
'''

#Suggested Approach
def merge_dicts(d1, d2):
    # Start with a copy of d1 to avoid modifying the original
    result = d1.copy()
    
    for key, value in d2.items():
        # .get(key, 0) returns 0 if the key doesn't exist yet
        result[key] = result.get(key, 0) + value
    
    return result

dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}

merged = merge_dicts(dict_a, dict_b)
print(f"Merged Dictionary: {merged}")

'''
WHY THIS IS BETTER:
- Non-destructive — originals are untouched.
- Wrapped in a function — reusable anywhere.
- Cleaner logic — result.get(key, 0) + value eliminates the need for an if/else entirely, since .get() returns 0 when the key doesn't exist yet.
- More Pythonic and concise.
'''
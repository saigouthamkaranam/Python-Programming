'''
Exercise 5: Flatten a Nested List
Practice Problem: Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements.
'''

def flatten(lst):
    flat_list = []

    for x in lst:
        if isinstance(x,list):
            flat_list.extend(flatten(x)) #using recursive call here.
        else:
            flat_list.append(x)
        
    return flat_list

nested_data = [1, [2, 3], [4, [5, 6]], 7]
result = flatten(nested_data)

print(f"Original:  {nested_data}")
print(f"Flattened List: {result}")
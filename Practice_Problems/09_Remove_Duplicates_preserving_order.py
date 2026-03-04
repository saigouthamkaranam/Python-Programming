'''
Practice Problem: Write a function that removes duplicate elements from a list. 
You cannot use set() because sets do not maintain the original order of elements.
'''

#My approach
# lst = [1, 2, 2, 3, 1, 4, 2]
# non_dup_lst = []
# for element in lst:
#     if element not in non_dup_lst:
#         non_dup_lst.append(element)
#     else:
#         pass
# print (non_dup_lst)


#More Efficient Approach

def remove_duplicates_ordered(items):
    seen = set()
    result = []
    
    for x in items:
        if x not in seen:
            result.append(x)
            seen.add(x)
            
    return result

# Usage
nums = [1, 2, 2, 3, 1, 4, 2]
print(f"Cleaned List: {remove_duplicates_ordered(nums)}") 


'''
Second Way is more efficient just the suggested approach is more efficient because 
it uses a set for lookups instead of a list! searching though set Time complexity is O(1) whereas 
in list its O(n) so if list is used overall time complexity becomes O(n squared) when list is used
overall time complexity stays O(n).
'''
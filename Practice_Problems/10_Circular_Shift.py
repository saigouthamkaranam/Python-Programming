'''
Practice Problem: Create a function rotate_list(lst, n, direction) that shifts 
the elements of a list by N positions. The direction can be left or right.
'''

def circular_shift(lst,shift,direction):
    
    shift = shift % len(lst)

    if direction == 'right':
        return lst[-shift:] + lst[:-shift]
    else:
        return lst[shift:] + lst[shift]



lst = [1, 2, 3, 4, 5] 
shift = 2
direction= 'right'

print(circular_shift(lst,shift,direction))

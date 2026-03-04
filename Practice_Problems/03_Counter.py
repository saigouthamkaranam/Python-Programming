'''
Exercise 3: Frequency Map with Counter
Practice Problem: Create a function that takes a string and returns a count of how many times each character appears. 
Ignore spaces and make it case-insensitive.
'''

import collections as col 

def Frequncy(text):
    result = col.Counter(text.lower())
    print(result)

text = input("Enter your text:\t")
Frequncy(text)
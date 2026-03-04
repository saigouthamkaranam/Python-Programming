'''
Practice Problem: Given a list of strings, use a single list comprehension 
to extract strings that meet two criteria: they must be longer than 5 characters 
AND they must start with a vowel (a, e, i, o, u).
'''
lst = ["apple", "education", "ice", "ocean", "python", "umbrella"]
vowels = ['a','e','i','o','u']
print([x for x in lst if (len(x)>5 and x[0] in vowels)])
'''
Exercise 4: Anagram Checker
Practice Problem: Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).
'''

is_Anagram = False

def Anagram_Checker(w1,w2):
    w1 = sorted(w1.lower())
    w2 = sorted(w2.lower())

    if w1 == w2:
        is_Anagram = True

    print(f'Is {word1} an anagram of {word2}? {is_Anagram}')

word1 = "Listen"
word2 = "silent"
Anagram_Checker (word1,word2)
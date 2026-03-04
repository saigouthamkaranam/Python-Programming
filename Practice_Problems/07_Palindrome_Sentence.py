'''
Practice Problem: Write a function to check if a full sentence is a palindrome.
You must ignore case, spaces, and all punctuation marks.
'''

def isPlaindromeSentence (sentence):
    sentence = sentence.lower()
    new_string =''
    for char in sentence:
        if char.isalnum() == True and char != ' ':
            new_string+=char

    if new_string == new_string[::-1]:
        isPlaindrome = True
    else:
        isPlaindrome = False

    print (isPlaindrome)
    
sentence = input("Please Enter your Sentence:")
isPlaindromeSentence(sentence)


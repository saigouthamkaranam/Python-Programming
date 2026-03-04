def longest_word_finder():
    sentence = input("Enter your sentence: ")
    sentence = sentence.split(' ')
    length = []

    for x in sentence:
        y = len(x)
        length.append(y)
    
    highest = max(length)
    
    return ''.join(x for x in sentence if len(x) == highest)

print(longest_word_finder())
    

'''
Bug / Edge case with this word:

return ''.join(x for x in sentence if len(x) == highest)

If two words have the same length it returns them joined together!

Input:  "I love coding python"
Output: "codingpython"  ❌ should be "coding" only
'''

#fix - Cleaner Version:
def longest_word_finder():
    sentence = input("Enter your sentence: ")
    words = sentence.split()

    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print(longest_word_finder())
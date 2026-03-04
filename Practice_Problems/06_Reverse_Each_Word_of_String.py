'''
Exercise 6: Reverse Each Word of a String
Practice Problem: Given a sentence, reverse each individual word within the string while maintaining the original word order.
'''

def Reverse_String ():
    word = (input("Enter Your text\t")).split(' ')
    print (' '.join(x[::-1] for x in word))
    
Reverse_String()

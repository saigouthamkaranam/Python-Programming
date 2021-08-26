#   1. Importing Random module

import random
#   2. Declaring the lists of required elements
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#   3. Greetings

print(" WELCOME TO GOUTHAM'S PASSWORD GENERATOR!!")

#   4. generating dynamic user inputs
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:

#   5. Create an epmty list to store password characters
password_list = []

#   6. using For loop
for char in range(1,nr_letters+1):
  random_char = random.choice(letters)
  password_list += random_char
for char in range(1,nr_numbers + 1):
  random_num = random.choice(numbers)
  password_list+= random_num
for char in range(1,nr_symbols +1):
  random_sym = random.choice(symbols)
  password_list += random_sym
random.shuffle(password_list)

#   7. this is the loop that converts elements in a List to a string 
password = ""
for char in password_list:
  password += char
print(f" Your Password is:\n {password}")

#THE END
#To know more about for loops in python and how to use them visit https://www.geeksforgeeks.org/python-for-loops/s
#To know more about Lists and random module in python and how to use them visit https://www.geeksforgeeks.org/python-list/ 
#Thank You ~K. SAI GOUTHAM. Visit my github profile for my projects https://www.githib.com/Gouthique
#To run this project Click on this link https://replit.com/@Gouthique/password-generator-start#main.py or you can run manually in your text editor.




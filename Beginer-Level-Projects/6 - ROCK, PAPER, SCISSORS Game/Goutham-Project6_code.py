#   1. importing the required Random Module

import random

#   2. generating The Ascii Art for ROCK - PAPER and SISSORS game to look it more realistic.
#   note that to generate multiline strings we use triple qoutes 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#   3. Putting those elements into the list
game = [rock,paper,scissors]

#   4. So here we know that lists index starts with 0 so basically the Rock index is 0 , paper and scissors indices are 1 and 2.
# delcaring a dynamic variable Choice to enter the coice
choice = int(input("Enter 0 to choose ROCK.\nEnter 1 to choose PAPER.\nEnter 2 to choose SCISSORS:\t"))

#   5. so list[index] is the syntax we use to pick the user choice which makes to choose from the rock/paper/sicssors.
#   6. synatx => game[choice]
 
#   7. Writing the rock-paper-sicssors win and lose conditions as code 

if choice <=2 and choice >=0:
  print(f"Your Choice:\n{game[choice]}")
  # 8. This statement picks one randomly from list game as we used random module and assigning to the variable.
  Goutham_choice = random.choice(game)
  print(f"Goutham chose:\n{Goutham_choice}")
  Gou_choice = game.index(Goutham_choice)
else:
  print(f"You Chose an Invalid Number {choice}!! Hence YOU LOSE!")
if choice <=2 and choice >=0:
  if (choice == 0) and (Gou_choice == 2):
    print("**************************\n\tCongratulations YOU WON\n**************************")
  elif (choice == 1) and (Gou_choice == 0):
    print("**************************\n\tCongratulations YOU WON\n**************************")
  elif (choice == 2) and (Gou_choice == 1):
    print("**************************\n\tCongratulations YOU WON\n**************************")
  elif (choice == Gou_choice):
    print("**************************\n\tOops Its a TIE\n**************************")
  else:
    print("**************************\n\tSorry YOU LOSE\n**************************")


#THE END
#To know more about if-statments in python and how to use them visit https://www.geeksforgeeks.org/python-if-else/#if
#To know more about Lists and random module in python and how to use them visit https://www.geeksforgeeks.org/python-list/ 
#Thank You ~K. SAI GOUTHAM. Visit my github profile for my projects https://www.githib.com/Gouthique
#To run this project Click on this link https://replit.com/@Gouthique/rock-paper-scissors-start#main.py or you can run manually in your text editor.

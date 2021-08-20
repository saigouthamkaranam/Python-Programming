
#1. WELCOME GREETING

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("WELCOME TO THE TREASURE ISLAND GAME.")
print("Your mission is to find the treasure.You will only have one life so use your instincts to find where the treasure is and ofcourse a hope that a pinch of luck favours you. GOOD LUCK!!") 

#2. DECLARING THE VARIABLES


start = input("\n\n\t\tto play the game type S to start")
start = start.lower()

#3. MAKING THE GAME THROUGH THE USE OF IF STATEMENTS

if start == 's':
  choice1 = int(input("You are walking Straight through a path of road and you have seen a key, what you do?\n1.Pick \n2. Leave \n(type your choice! either 1 or 2):\t"))
  if choice1 == 1:
    print(''''
               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--'
               ''')
    print('Good we have got our key')
    choice2 = int(input("\nNow you continue walking futher and come across a forest. You now found another key!! what you do?\n1.Pick \n2. Leave \n(type your choice! either 1 or 2):\t"))
    if choice2 == 1:
      print ("\n\nwelldone lets Move futher. You have passed the forrest and now you see a castle")
      choice3 = int(input("You have entered the castle. The castle is so huge and it has 72 rooms in it.So u have gone near the first room. What you will do?\n1. knock the door politely\n2. bang the door/open it forcefully?\n(type your choice! either 1 or 2):\t"))
      if choice3 == 1:
        print("Good JOB")
        print('''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|''')
        choice4 = int(input("\n\nA man opens the door and asks for the key, You gave him one key then he returned you two other keys!! Like this you have repeated the same for other 70 rooms!!\n The man In the last room has asked to give all the keys that he has recived from the previous 71 rooms and you have given to him!! Now he gives you two last keys and he wants to walk you through the secret passage with him. What you will do? \n1. Walk with him\n2. kill him\n(type your choice! either 1 or 2):\t"))
        if choice4 == 1:
          choice5 = int(input("\n\nnow he takes you into the huge room which has 10 big lockers in it and tells you that The number of keys you have left is the locker number that has treasure!! SO how many number of keys do u have?\n(type your choice! either numbers):\t"))
          if choice5 == 3:
            print("\n\n\t\t\tCongratulations YOU HAVE WON THE GAME!! the treasure is yours")
            print("\t\t`/ () |_|   \/\/ () |\| ")
          else:
            print("\n\nThe castle has been KABOOM!! U have opened a wrong door by choosing wrong number!\n WISH YOU COULD HAVE PICKED THE KEY IN THE FOREST SO THAT YOU HAD LEFT WITH 3 KEYS IN TOTAL!!!")
            print("(_,   /\   |\/|   [-     () \/   [-   /?")
        else:
          print("\n\nYou have been cursed to death since u have killed the innocent!")
          print("(_,   /\   |\/|   [-     () \/   [-   /?")

      else:
        print("\n\nThe people inside the castle got scared and they shot u with a gun. You are DEAD")
        print("(_,   /\   |\/|   [-     () \/   [-   /?") 
    else:
      print ("\n\nwelldone lets Move futher. You have passed the forrest and now you see a castle")
      choice3 = int(input("You have entered the castle. The castle is so huge and it has 72 rooms in it.So u have gone near the first room. What you will do?\n1. knock the door politely\n2. bang the door/open it forcefully?\n(type your choice! either 1 or 2):\t"))
      if choice3 == 1:
        print("Good JOB")
        print('''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|''')
        choice4 = int(input("\n\nA man opens the door and asks for the key, You gave him one key then he returned you two other keys!! Like this you have repeated the same for other 70 rooms!!\n The man In the last room has asked to give all the keys that he has recived from the previous 71 rooms and you have given to him!! Now he gives you two last keys and he wants to walk you through the secret passage with him. What you will do? \n1. Walk with him\n2. kill him\n(type your choice! either 1 or 2):\t"))
        if choice4 == 1:
          choice5 = int(input("\n\nnow he takes you into the huge room which has 10 big lockers in it and tells you that The number of keys you have left is the locker number that has treasure!! SO how many number of keys do u have?\n(type your choice! either numbers):\t"))
          if choice5 == 3:
            print("\n\n\t\tCongratulations YOU HAVE WON THE GAME!! the treasure is yours")
            print("\t\t`/ () |_|   \/\/ () |\| ")
          else:
            print("\n\nThe castle has been KABOOM!! U have opened a wrong door by choosing wrong number!\n WISH YOU COULD HAVE PICKED THE KEY IN THE FOREST SO THAT YOU HAD LEFT WITH 3 KEYS IN TOTAL!!!")
            print("(_,   /\   |\/|   [-     () \/   [-   /?")
        else:
          print("\n\nYou have been cursed to death since u have killed the innocent!")
          print("(_,   /\   |\/|   [-     () \/   [-   /?")

      else:
        print("\n\nThe people inside the castle got scared and they shot u with a gun. You are DEAD")
        print("(_,   /\   |\/|   [-     () \/   [-   /?")          
  else:
    print("\n\nGAME OVER!!! You didnt pick the most important thing required for the game")
    print("(_,   /\   |\/|   [-     () \/   [-   /?")

#THE END
#To know more about if-statments in python and how to use them visit https://www.geeksforgeeks.org/python-if-else/#if
#Thank You ~K. SAI GOUTHAM. Visit my github profile for my projects https://www.githib.com/Gouthique
#To run this project Click on this link https://replit.com/@Gouthique/treasure-island-start#main.py or you can run manually in your text editor.

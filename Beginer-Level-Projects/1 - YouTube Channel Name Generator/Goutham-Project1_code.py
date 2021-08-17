#1. Create a greeting for your program.
#You can do this by using The Python Print Statement!

print("YOUTUBE NAME GENERATOR") 

#2. Ask the user for the company.
#python input function

A = input("Please enter your Company/the first name you want to put:\n")

#3. Ask the user for the category.
#Python Lists

mylist = [" ","Studios","LLC","INC","Organization","Co","company","Foods","Club","Tech","Geeks","Comics House"]
print("please select your end name tag from the list below")
print ("1.Studios\n2.LLC\n3.INC\n4.Organization\n5.Co\n6.company\n7.Foods\n8.Club\n9.Tech\n10.Geeks\n11.Comics House\n0.none")
Category = input("please select the catergory of the channel from above")

#4. storing the value
#Using variables
value = mylist[int(Category)]
F = value

#5. printing out the output!
#using print statment

print("Your YouTube Name is generated\n"+ A + " " + F)
# You can run my project from here: https://replit.com/@Gouthique/YouTibe-name-generator-start-1#main.py

#THANK YOU! ~K. SAI GOUTHAM
#Visit my github page for my projects https://github.com/Gouthique
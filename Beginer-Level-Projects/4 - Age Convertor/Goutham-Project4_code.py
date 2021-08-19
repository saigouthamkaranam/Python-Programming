
#1. GREETING WITH PYTHON PRINT FUNCTION

print ("Welcome Know your age in months,weeks,days,and hours")

#2. DECLARING VARIABLES
'''
Age = that stores the age
inyears = stores the age in years
inweeks = using formula to convert the current age in years to weeks
inmonths = using formula to convert the current age into months 
indays= using formula to convert the current age in years to days
inhours = using formula to convert the current age into hours
'''
age = int(input("enter your age"))
inyears = age
inmonths = age * 12 
inweeks = inmonths * 52
indays= inweeks * 365
inhours = indays * 24

#3. Printing to the standard output 

print(f"your age in years:\t{inyears} years\nyour age in months:\t{inmonths} months \nyour age in weeks: {inweeks} weeks \nyour age in days:\t{indays} days \nyour age in hours:\t{inhours} hours")

#4. Calculating the End age in the same manner

Endage = int(input("Enter your assemed end age! for example:100 years"))
Endage = Endage - age
Einyears = Endage
Einmonths = Endage * 12 
Einweeks = Einmonths * 52
Eindays= Einweeks * 365
Einhours = Eindays * 24
print(f"your remaining age in years:\t{Einyears} years \nyour remaining age in months:\t{Einmonths} months \nyour remaining age in weeks: {Einweeks} weeks \nyour remaining age in days:\t{Eindays} days \nyour remaining age in hours:\t{Einhours} hours")
print("Thanks For using Goutham's age convertor")

# THE END
#I am using F-strings to print several variables values because:-> String concatination only works with string we cannot concatinate String and Int.
#To know more about F-strings and how to use them visit https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python
#Thank You ~K. SAI GOUTHAM. Visit my github profile for my projects https://www.githib.com/Gouthique
#To run this project Click on this link https://replit.com/@Gouthique/ageconvertor-3 or you can run manually in your text editor.
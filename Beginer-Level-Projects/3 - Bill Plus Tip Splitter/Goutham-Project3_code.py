
#1. GREETING WITH PYTHON PRINT FUNCTION
print ("************Hello Welcome to Bill Spliter*****************\n\n")

#2. DECLARING VARIABLES
total = (input("\tplease enter the total bill amount:\t"))
total = int(total)
n = int(input("\n\tEnter no.of people that the bill to be splitted to:\t"))

#3. ASSIGNING VALUES TO THOSE VARIABLES
isTip = int(input("\n\tIf want to add the some tip then select the any one from 5% or 10% or 15% \n\tIf u do not want to add tip then please enter '0'\t"))
isTip = round(isTip/100 + 1,2)

#4 THE TOTAL AMOUNT ADDED WITH THE TIP AMOUNT
withTip = round(total * isTip,2) 

#5 FINAL VALUE THAT EACH PERSON SHOULD PAY
Final_value = round(withTip / n,2)
print (f"\n\tYour total amount is:\t{total} \n\tTotal amount on adding tip: \t{withTip} \n\tEach member should pay: \t{Final_value}")
print("\n\tThanks for using Goutham's Bill plus Tip Splitter")

#Thank You ~K. SAI GOUTHAM. Visit my github profile for my projects https://www.githib.com/Gouthique
#To run this project Click on this link https://replit.com/@Gouthique/BillSplitterwithtip-1#main.py or you can run manually in your text editor.
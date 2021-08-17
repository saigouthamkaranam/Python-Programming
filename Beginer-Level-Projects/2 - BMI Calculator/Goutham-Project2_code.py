#1. greeting Using print Statement
print("Hello Welcome to BMI calculator")
print(
    "to know your BMI value tell us your Weight in kilograms and height in centimeters"
)

#2. Declaring the variables
'''
Declaring Three variables:
height - for heignt in cm
weight - for weight input in kg
BMI - to calculate the bmi using the BMI formula  

'''
height = float(input("please enter your height in cm"))
weight = float(input("please enter your height in kilograms (kg)"))
Bmi = round(weight / (height * height) * 10000, 2)

#4. Printing the BMI value 
print(f"your body mass index is {Bmi}")

#5. where you stand if you dont understand the if statments just dont remove the pair of (''' ''') at the start and end of the lines.
#HOWEVER IF YOU WISH TO UNDERSTAND AND USE IT remove the pair of tripele quotes and run it!!

'''
if (Bmi < 18.5):
    {
        print(
            "You are Underweight, You need to gain weight and improve your health"
        )
    }
elif ( 18.5 < Bmi < 24.9):
    {print("You are Normal Weight, Congratulations you are healthy!!")}
elif ((25.0 < Bmi < 29.9)):
    {
        print(
            "You are Over Weight, You need to loose some weight and improve your health"
        )
    }
elif ((Bmi >= 30.0)):
    {print("You are Obese, OMG you need to improve health")}
else:
    {print("Oops please enter proper values of your height and weight")}
print("THANK YOU FOR USING GOUTHAM'S BMI CALCULATOR")
'''
#Thank You ~K. SAI GOUTHAM - Visit my github for my projects - https://www.github.com/Gouthique
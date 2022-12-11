#Write a program that interprets the BMI based on a user's weight and height.

#it should tell them the interpretation of their BMI based on the BMI value.

#under 18.5 they are underweight
#over 18.5 but below 25 they have a normal weight
#over 25 but below 30 they are overweight
#over 30 but below 35 they are obese
#above 35 they are clinically obese.

#Don't change the code below.
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#write the code below this line
bmi = int(int(weight) / float(height) ** 2)
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are under weight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are over weight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, You are obese.")
else:
    print(f"Your Bmi is {bmi}, You are clinically obese.")
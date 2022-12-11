#write a program that calculate the Body Mass Index (BMI) form user's weight and height.

#Don't change the code below
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
#write your code below this line
bmi = int(int(weight) / float(height) ** 2)
print(bmi)

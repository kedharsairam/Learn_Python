#Create a program using maths and f-strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#it will take your current age as the input and output a message with our time format left in this format.
#Dont's change the code below
age = input("What is your current age?")
#write your code from here.
r_age = 90 - int(age)
days = r_age * 365
weeks = r_age * 52
months = r_age * 12
result = (f"you have {days} days, you have {weeks} weeks, you have {months} months left.")
print(result)
#Write a program that out whether if a given number is an odd or even number.
#don't change the code below.
number = int(input("Which number do you want to check?"))
#write you code below this line.
num = number % 2
if num == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")
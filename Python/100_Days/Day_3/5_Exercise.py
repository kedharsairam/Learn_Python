#write a program that works out whether if a given year is a leap year.

#don't change the code below
year = int(input("Which year do you want to check?"))
#write your code below this line
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not a Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not a Leap Year.")
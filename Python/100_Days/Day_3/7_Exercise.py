#write a program for ordering pizza.

#small pizza: $15
#medium pizza: $20
#large pizza: $25

#pepperoni for small pizza: +$2
#pepperoni for medium or large pizza: +$3

#extra cheese for any size pizza: +$1

#don't change the code below.
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L. ")
pepperoni = input("Do you want Pepperoni? Y or N. ")
cheese = input("Do you want extra cheese? Y or N. ")
#write your code below this line
bill = 0

if size == 'S':
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
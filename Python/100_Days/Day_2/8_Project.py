#write a program for a tip calculator.
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
t_bill = tip / 100 * bill + bill
result = round(t_bill, 2)
result = "{:.2f}".format(t_bill)
result = t_bill / people
print(f"Each person should pay: ${result}")
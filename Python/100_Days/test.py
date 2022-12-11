print("Welcome to kedish pizza deliveries!")
size = input("what size pizza do you want? S, M, or L: ").lower()
cheese = input("do you want extra cheese? Y or N: ").lower()
bill = 0
if size == 'S':
    bill += 150
elif size == "M":
    bill += 200
else:
    bill += 250
if cheese == "Y":
    bill += 30
print(f"Your final bill is: Rs.{bill}.")
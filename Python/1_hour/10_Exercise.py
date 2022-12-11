weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ").lower()
if unit == "k":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))
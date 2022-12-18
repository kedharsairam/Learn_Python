weight = int(input("Weight: "))
unit = str(input("(L)bs or (K)g: ")).lower()
if unit == "l":
    x = weight * 0.45
    print(f"You are " + str(round(x)) + " Pounds")
if unit == "k":
    y = weight / 0.45
    print(f"You are " + str(round(y)) + " Pounds")
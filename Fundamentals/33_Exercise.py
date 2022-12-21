num1 = [2,2,3,3,5,7,8,3,3,7]
num2 = []
for number in num1:
    if number not in num2:
        num2.append(number)
print(num2)
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be Zero.")
except ValueError:
    print("Invalid Value")
    
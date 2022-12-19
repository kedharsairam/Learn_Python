secret = 7
guess = 0
limit = 3
while guess < limit:
    g = int(input("Guess: "))
    guess += 1
    if g == secret:
        print("You Won!")
        break
else:
    print("You Failed!")
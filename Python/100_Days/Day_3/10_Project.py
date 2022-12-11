#write a program for a simple tressure island game.
#don't change the code below.
print("Welcome to Tressure Island.")
print("Your mission is to find the tressure.")
#write your code from this line.
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input('You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?').lower()
        if choice3 == "red":
            print("it's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
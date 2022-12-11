names = ["kedhar", "sairam", "kkd", "i don't know"]
print(names)
print(names[0])
# to print out the first name.
print(names[-1])
#to print out the last name.
names[0] = "KEDHAR"
#to change the name.
print(names)
print(names[0:3])
#to print out a range of names.


numbers = [1, 2, 3, 4, 5]
numbers.append(6)
#to add something int he end.
print(numbers)
numbers.insert(0, -1)
#to add something in a specific position.
print(numbers)
numbers.remove(3)
#to remove the specific item in the list.
print(len(numbers))
#to find out number of items int he list.
print(numbers)
numbers.clear()
#to clear everything in the list.
print(numbers)
print(1 in numbers)
#this is to find out something in the list.
#it's a boolean value.
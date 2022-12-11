num_char = len(input("What is your name?"))
print(type(num_char))
#"type" is a function which is used to find out the type of the data we have.

new_num_char = str(num_char)
#for changing the datatype, integer into string. we use this...
#we can convert any datatype to any datatype by just using the datatype as a function and put the value in parenthesis.

print("Your name have " + new_num_char + " characters.")
#we con't directly print out the string and integer together.
#we con't also print out the number of characters with len function.

#for example
a = str(12)
print(type(a))

b = float(34)
print(type(b))

print(70 + 100)

print(70 + float("100.5"))

print(str(70)+str(100))
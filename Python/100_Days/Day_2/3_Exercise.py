#write a program that adds the digits in a 2 digit number. 
#e.g. if the input was 35, then the output should be 3 + 5 = 8

#warning. Do not change the code on line 7. your program should work for different inputs.
#e.g. any two-digit number.

two_digit_number = input("Type a two digit number: ")
#write the code below this...
first_num = (two_digit_number[0])
second_num = (two_digit_number[1])
result = int(first_num) + int(second_num)
print(result)
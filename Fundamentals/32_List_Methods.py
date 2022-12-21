numbers = [ 5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)


numbers.insert(0, 10)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(2))

print(50 in numbers)

numbers.clear()
print(numbers)

num = [5,2,5,3,4,7]
print(num.count(5))

num.sort()
print(num)

num.reverse()
print(num)

num2 = num.copy()

num.append(10)
print(num)
print(num2)
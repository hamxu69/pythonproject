numbers = [1,2,3,4,5,6,7,8,9,10]
names = ["Hamza", "Ali", "Ahmed", "Usman"]
squares = [num * num for num in numbers]
odd = [num for num in numbers if num % 2 != 0]
even = [num for num in numbers if num % 2 == 0]
upper_case = [word.upper() for word in names]
print(squares)
print(odd)
print(even)
print(upper_case)

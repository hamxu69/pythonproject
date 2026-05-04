# Basic Python Snippets
practice = 5
print(practice)
# 1. Hello World
print(f"Practice makes perfect! You have practiced {practice} times.")

# 2. Variables and Data Types
x = 5  # int
y = 3.14  # float
name = "Python"  # str
is_true = True  # bool

print(f"x: {x}, y: {y}, name: {name}, is_true: {is_true}")

# 3. Lists
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(f"List: {my_list}")

# 4. Tuples
my_tuple = (1, 2, 3)
print(f"Tuple: {my_tuple}")

# 5. Dictionaries
my_dict = {"key1": "value1", "key2": "value2"}
my_dict["key3"] = "value3"
print(f"Dict: {my_dict}")

# 6. If Statements
if x > 3:
    print("x is greater than 3")
else:
    print("x is not greater than 3")

# 7. Loops
# For loop
for i in range(5):
    print(f"For loop: {i}")

# While loop
count = 0
while count < 3:
    print(f"While loop: {count}")
    count += 1

# 8. Functions
def greet(name):
    return f"Hello, {name}"

print(greet("World"))

# 9. Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"I am {self.name}, {self.age} years old."

person = Person("Alice", 30)
print(person.introduce())

# 10. File I/O
# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, file!")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print(f"File content: {content}")

# 11. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 12. List Comprehensions
squares = [i**2 for i in range(10)]
print(f"Squares: {squares}")

# 13. Lambda Functions
add = lambda a, b: a + b
print(f"Add 2+3: {add(2, 3)}")

# 14. Modules (importing)
import math
print(f"Pi: {math.pi}")

# 15. Input
# user_input = input("Enter something: ")
# print(f"You entered: {user_input}")  # Commented out to avoid blocking

print("Basic Python snippets covered!")
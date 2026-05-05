# 1. Print your name, age, and city on 3 separate lines.
# 2. Store your name in a variable and print:
# Hello, [your name]!
# 3. Store two numbers, add them, and print the result.
# 4. A shirt costs 500 PKR. You're buying 3. Print the total cost.
# 5. Store your birth year. Calculate and print your age.
# 1
print("Hamza")
print("21")
print("Lahore")
# 2
name = "Hamza"
print(f"Hello, {name}")
# 3
a = 2
b = 4
sum = a + b
print(f"The sum of {a} and {b} is {sum}")
# 4
shirt = 500
quantity = 3
total = shirt * quantity
print(f"{total} is your total")
# 5
my_age = int(input("Enter your birth year: "))
current_year = 2026
yearsOld = current_year - my_age
print(f"You're {yearsOld}!")
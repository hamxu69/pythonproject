# 6. Ask the user for their name, then print Hello, [name]! Welcome.
# 7. Ask for two numbers and print their sum, difference, product, and division.
# 8. Ask for a temperature in Celsius, convert it to Fahrenheit, print the result.

# Formula: F = (C × 9/5) + 32

# 9. Ask for someone's birth year, print how old they are.
# 10. Ask for a price and a discount percentage, print the final price after discount.
# 6
userName = input("State your name here:")
print(f"Hello, {userName}! Welcome.")
# 7
a = int(input("Enter a number:"))
b = int(input("Enter a again number:"))
sum = a + b
product = a * b
difference = a - b
division = a / b
print(f"sum of following numbers is {sum}")
print(f"product of following numbers is {product}")
print(f"difference of following numbers is {difference}")
print(f"division of following numbers is {division}")
# 8
TemperatureInCelsius = int(input('Enter Temperature:'))
InFahrenheit = (TemperatureInCelsius * 9/5) + 32
print(f"Temperature in Fahrenheit is {InFahrenheit}'F.")
# 9
userAge = int(input("Enter your birth year: "))
current_year = 2026
outputAge = current_year - userAge
print(f"You're {outputAge}!")
# 10
ogPrice = int(input("Price of watch: "))
discountPer = int(input("Discount Percentage: "))
discountPrice = (discountPer/100) * ogPrice
finalPrice = ogPrice - discountPrice 
print(finalPrice)


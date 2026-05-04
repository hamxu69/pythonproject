name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age < 18:
    body = "a Minor"
else:
    body = "an Unc"
print(f"Hello, {name}! you are {age} old, Practically {body}!")
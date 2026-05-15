students = []

while True:

    name = input("Enter your name: ")

    if name == "exit":

        print("\n--- STUDENT RECORDS ---")

        for i in students:
            print(f"""
Name: {i["name"]}
Marks: {i["marks"]}
Grade: {i["grade"]}
""")

        break

    marks = int(input("Enter your marks: "))

    grade = ""

    if marks >= 90:
        grade = "A"

    elif marks >= 70:
        grade = "B"

    elif marks >= 50:
        grade = "C"

    else:
        grade = "F"

    student = {
        "name": name.title(),
        "marks": marks,
        "grade": grade
    }

    students.append(student)
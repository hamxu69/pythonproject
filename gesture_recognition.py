students = []
student = {
    "name": "",
    "marks": "",
    "grade": ""
}
while True:
    name = input("Enter your name: ")
    if name == 'exit':
        for i in students:
            print(f"name: {i["name"]}")
        break
    marks = int(input("Enter your marks: "))
    grade = ''
    if marks >= 90:
        grade = "A"
        student["name"] = name.title()
        student["marks"] = marks
        student["grade"] = grade
        
    elif marks >= 70:
        grade = "B"
        student["name"] = name.title()
        student["marks"] = marks
        student["grade"] = grade
        
    elif marks >= 50:
        grade = "C"
        student["name"] = name.title()
        student["marks"] = marks
        student["grade"] = grade
        
    elif marks < 50:
        grade = "F"
        student["name"] = name.title()
        student["marks"] = marks
        student["grade"] = grade
    students.append(student)

students = []

while True:
    options = input("""1. Add Student
2. Search Student
3. Show All Students
4. Exit
                    """)
    if options == "4":
        print("Program Ended")
        break
    if options == "2":
        search_name = input("Enter student name:").title()
        for i in students:
            if search_name == {i[name]}:
                            print(f"""
Name: {i[name]}
Marks: {i[marks]}
Grade: {i[grade]}
""")
            else: 
                print("Student doesn't exists")
    if options == "3":
        if len(students) != 0:
            for i in students:
                            print(f"""
Name: {i[name]}
Marks: {i[marks]}
Grade: {i[grade]}
""")
        else:
            print("Student data doesn't exist")        
    name = input("Enter your name:")
    marks = int(input("Enter your marks:"))
    if marks >= 90:
        grade = "A"
    if marks > 70:  
        grade = "B"
    if marks >= 60:  
        grade = "C"
    if marks < 50:  
        grade = "F"
    student = {
        "name": name.title(),
        "marks": marks,
        "grade": grade
    }
    students.append(students)

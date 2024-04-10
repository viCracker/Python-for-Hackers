students = {"Mark": "A", "Tom": "B"}

print(students)


on = True
while on:
    student = input("Enter student name: ")
    grade = input("Grade: ")
    students[student] = grade
    print(students)
    add_student = input("Add Another?(Y/N): ").lower()
    if add_student == "y":
        pass
    else:
        print("Goodbye!")
        on = False

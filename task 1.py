student_marks = {
    "Yash": 85,
    "Prathamesh": 92,
    "Vivek": 78,
    "Dev": 88,
    "Jidnesh": 90
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")

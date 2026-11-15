# Complete Python Code
from functools import reduce

students = [
    {"name": "Anshul", "marks": 92},
    {"name": "Rahul", "marks": 75},
    {"name": "Aman", "marks": 45},
    {"name": "Priya", "marks": 88},
    {"name": "Rohit", "marks": 60},
    {"name": "Neha", "marks": 96}
]


# 1. Pure function: Check pass status
def is_passed(student):
    return student["marks"] >= 40


# 2. Pure function: Calculate grade
def calculate_grade(student):
    marks = student["marks"]

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    return {
        "name": student["name"],
        "marks": marks,
        "grade": grade
    }


# 3. Filter passed students
passed_students = list(filter(is_passed, students))


# 4. Calculate grades
graded_students = list(map(calculate_grade, passed_students))


# 5. Find high performers
high_performers = list(
    filter(lambda student: student["marks"] >= 80, graded_students)
)


# 6. Calculate class average
total_marks = reduce(
    lambda total, student: total + student["marks"],
    students,
    0
)

average = total_marks / len(students)


# 7. Find topper
topper = reduce(
    lambda best, student:
        student if student["marks"] > best["marks"] else best,
    students
)


# 8. Generate report
def generate_report():
    print("\n===== STUDENT PERFORMANCE REPORT =====")

    print("\nPassed Students:")

    for student in graded_students:
        print(student)

    print("\nHigh Performers:")

    for student in high_performers:
        print(student["name"], "-", student["marks"])

    print("\nClass Average:", round(average, 2))

    print("\nClass Topper:")
    print(topper["name"], "-", topper["marks"])

    print("\nTotal Students:", len(students))
    print("Passed Students:", len(passed_students))
    print("Failed Students:", len(students) - len(passed_students))


generate_report()

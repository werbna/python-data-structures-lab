# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    students = ['Alice', 'Bob', 'Charlie']
    first_student = students[1]
    last_student = students[-1]
    return students, first_student, last_student

students, first_student, last_student = manage_students()
print('Exercise 1: Students:', students)
print('Exercise 1: First student:', first_student)
print('Exercise 1: Last student:', last_student)
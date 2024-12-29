# empty dictionay for student marks
student_marks = {}

number_of_student = int(input("Enter the number of students: "))

# taking inputs for name and marks
for i in range(number_of_student):
    name = input(f"Enter the name of student {i+1}: ")
    marks = float(input(f"Enter marks for {name}: "))
    student_marks[name] = marks

# the mean of marks
mean_marks = sum(student_marks.values()) / len(student_marks)

print("\nStudent Marks:", student_marks)
print("Mean of the marks:", mean_marks)


n = int(input("Enter number of students: "))
k = int(input("Enter number of scholarships: "))

eligible_students = []

for i in range(n):
    print("\nEnter details for student", i + 1)

    student_id = input("Enter student ID: ")
    cgpa = float(input("Enter CGPA: "))
    income = float(input("Enter family income: "))

    if cgpa >= 8.5 and income <= 300000:
        eligible_students.append(student_id)

print("\nEligible students:")

for student_id in eligible_students:
    print(student_id)

print("\nNumber of eligible students:", len(eligible_students))

print("\nStudents selected for scholarship:")

for i in range(min(k, len(eligible_students))):
    print(eligible_students[i])

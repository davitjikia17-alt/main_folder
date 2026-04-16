n = int(input("Enter number of students: "))

grades = []


for i in range(n):
    grade = float(input(f"Enter grade for student {i+1}: "))
    grades.append(grade)


average = sum(grades) / n


count = 0
for grade in grades:
    if grade > average:
        count += 1

print("Number of accepted students:", count)
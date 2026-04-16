names = []
gradeA = []
gradeB = []
gradeC = []

# input data
for i in range(25):
    name = input(f"Enter name of student {i + 1}: ")
    g1 = float(input("Enter first exam grade: "))
    g2 = float(input("Enter second exam grade: "))

    names.append(name)
    gradeA.append(g1)
    gradeB.append(g2)

    # find higher grade WITHOUT max()
    if g1 > g2:
        gradeC.append(g1)
    else:
        gradeC.append(g2)

# print results
for i in range(25):
    print("Name:", names[i])
    print("First grade:", gradeA[i])
    print("Second grade:", gradeB[i])
    print("Final grade:", gradeC[i])
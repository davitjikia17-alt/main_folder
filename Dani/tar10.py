def count_high_scores(score1, score2, score3):
    count = 0
    if score1 >= 90:
        count += 1

    if score2 >= 90:
        count += 1

    if score3 >= 90:
        count += 1

    return count

def main():
    eligible_students = []
    n = int(input("Enter number of students:"))

    for i in range(n):
        name = input("Enter student name:")
        score1 = int(input("Enter score1:"))
        score2 = int(input("Enter score2:"))
        score3 = int(input("Enter score3:"))

        if count_high_scores(score1, score2, score3) == 3:
            eligible_students.append(name)

    print("Students eligible for the national competition:")
    for student in eligible_students:
        print(f"{student}")

    print(f"Total number of eligible students: {len(eligible_students)}")

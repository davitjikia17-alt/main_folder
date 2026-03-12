def grading():
    count_90 = 0
    for i in range(3):
        grade = int(input("enter grade:"))
        if grade >= 90:
            count_90 += 1
    return count_90



def main():
    count = 0
    while True:
        name = input("enter your name:")
        count_90 = grading()
        if count_90 == 3:
            count += 1
        print("got accepeted",name)
        print("sum of people",count)


main()
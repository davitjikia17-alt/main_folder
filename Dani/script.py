def tar(month, year):
    if month <= 6 and month >= 1 and year == 2009 :
        return True
    return False



def main():
    count_girl = 0
    count_boy = 0
    for i in range(1000):
        gender = int(input("Enter your gender /1 boy , /2 girl:"))
        month = int(input("please enter  month:"))
        year = int(input("please enter  year:"))
        use = tar(month, year)
        if use == True and gender == 1:
            count_boy += 1
        if use == True and gender == 2:
            count_girl += 1

    print(f"boys:{count_boy}")
    print(f"girl:{count_girl}")

main()
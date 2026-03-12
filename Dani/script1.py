def main():
    costumer = int(input("enter year of clubbing: "))
    spent = int(input("enter amount spent monthly: "))
    count = 0
    for i in range(5000):
        if costumer >= 3 and spent >= 1200:
            if costumer <= 8:
                print("50 shekels cupon")
                count += 1
            if costumer >= 8:
                print("100 shekels cupon")
                count += 1
        else:
            print("0 shekels cupon")

    print("people who got cupon=",count)
main()
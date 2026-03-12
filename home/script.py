def main():
    count = 0
    while True:
        for i  in range (492):
            age = input("Enter your age: ")
            hour = input("Enter your hours spent: ")
            if age <= 18 and age >= 15 and hour >= 3:
                count += 1
        break
    print("people who is true ",count)

main()
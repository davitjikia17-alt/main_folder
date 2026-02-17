def add(numbers):
    result = 0
    for i in numbers:
        result += i
    print(result)

def minus(numbers):
    result = 0
    for i in numbers:
        result -= i
    print(result)

def multiply(numbers):
    result = 0
    for i in numbers:
        result *= i
    print(result)

def divide(numbers):
    pass

def main():
    numbers = []
    while True:
        num = int(input("enter numbers:"))
        numbers.append(num)
        if num == 999:

            break
    sing = input("+,-,/,* ==>")
    if sing == "+":
        add(numbers)
    elif sing == "-":
        minus(numbers)
    elif sing == "*":
        multiply(numbers)
    elif sing == "/":
        divide(numbers)

main()
import random

def how_many_until_double(sides):
    count = 0
    while True :
        count += 1

        first_cube = random.randint(1,sides)
        second_cube = random.randint(1,sides)
        if first_cube == second_cube:
            return count
def how_many_until_roles(roles):
    total = 0
    for i in range (roles):
        result = how_many_until_double(sides)
        total += result
    return total / roles

how_many = int(input("How many roles do you have?"))
sides = int(input("enter number:"))
print("averege:")
print(how_many_until_roles(how_many))

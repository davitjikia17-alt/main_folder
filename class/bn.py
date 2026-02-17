import random
first_cube = random.randint(1,6)
second_cube = random.randint(1,6)

count = 1
while first_cube != 6 or second_cube != 6:
    print(f"first_cube: {first_cube}")
    print(f"second_cube: {second_cube}")

    first_cube = random.randint(1,6)
    second_cube = random.randint(1,6)

    count += 1
print(count)

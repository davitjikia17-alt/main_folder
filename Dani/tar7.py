numbers = []


for i in range(20):
    num = float(input(f"Enter grade {i+1}: "))
    numbers.append(num)

pass_list = []
fail_list = []

for num in numbers:
    if num > 55:
        pass_list.append(num)
    else:
        fail_list.append(num)


print("Passing grades:", pass_list)
print("Failing grades:", fail_list)
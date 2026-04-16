numbers=[17,1,20,20,4,55,55,55,72,88,88,94]
count = 0
for index in range(len(numbers)-1):
    if numbers[index] == numbers[index+1]:
        count = count + 1
print("count=",count)


# count = 4
# it counts if index and next index is equal
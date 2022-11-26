def two_sum(numbers, target):
    for i in range(0,len(numbers)):
        for j in range(1,len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i,j]

print(two_sum([2,2,3], 4))
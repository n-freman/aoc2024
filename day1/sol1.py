with open('input1.txt.bak') as file:
    lines = file.readlines()

arr = []
arr1 = []
for line in lines:
    i, j = tuple(map(int, line.strip().split()))
    arr.append(i)
    arr1.append(j)

arr.sort()
arr1.sort()

total_diff = 0
for i, j in zip(arr, arr1):
    total_diff += abs(i - j)

print(total_diff)


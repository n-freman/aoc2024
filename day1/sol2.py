from collections import Counter


with open('input1.txt') as file:
    lines = file.readlines()

arr = []
arr1 = []
for line in lines:
    i, j = tuple(map(int, line.strip().split()))
    arr.append(i)
    arr1.append(j)

arr.sort()
arr1.sort()

arr1_counts = Counter(arr1)

total = 0
for i in arr:
    total += i * arr1_counts.get(i, 0)
print(total)


from pprint import pprint as print
from collections import Counter

with open('input1.txt') as file:
    lines = file.readlines()

arr = []
for line in lines:
    arr.append(list(map(int, line.strip().split())))

count = 0


def check_numbers(numbers) -> bool:
    if single_check(numbers):
        return True
    for i in range(len(numbers)):
        new_numbers = numbers.copy()
        new_numbers = new_numbers[:i] + new_numbers[i+1:]
        if single_check(new_numbers):
            return True
    return False


def single_check(numbers) -> bool:
    differences = []
    for i in range(1, len(numbers)):
        differences.append(numbers[i] - numbers[i-1])
    if not 1 <= max(list(map(abs, differences))) <=3:
        return False
    if len(list(filter(lambda i: i == 0, differences))) > 0:
        return False
    diff_sign = list(map(lambda i: i > 0, differences))
    if all(diff_sign) or not any(diff_sign):
        return True
    return False


for line in arr:
    count += check_numbers(line)

print(count)


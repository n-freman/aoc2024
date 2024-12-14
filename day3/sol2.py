import re

with open('./input1.txt') as file:
    lines = file.readlines()

pattern = re.compile(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))")

total = 0

enabled = True
for line in lines:
    for match in pattern.findall(line):
        print(match, enabled)
        if match[2] == "" and enabled:
            total += int(match[0]) * int(match[1])
        else:
            if match[2] == 'do()':
                enabled = True
            if match[2] == "don't()":
                enabled = False


print(total)


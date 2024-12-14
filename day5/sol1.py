import math

with open('input1.txt') as file:
    rules = []
    while line := file.readline():
        if line == '\n': break
        rules.append(tuple(line.strip().split('|')))
    
    updates = []
    while line := file.readline():
        updates.append(line.strip().split(','))


result = 0
for row in updates:
    for i in range(1, len(row)):
        num = row[i]
        is_ok = True
        for rule in rules:
            if rule[0] == num:
                try:
                    if row.index(rule[1]) < i:
                        is_ok = False
                        break
                except ValueError:
                    pass
        if not is_ok:
            break
    else:
        result += int(row[len(row)//2])

print(result)


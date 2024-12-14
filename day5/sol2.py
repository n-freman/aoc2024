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
rows_to_fix = []
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
            rows_to_fix.append(row)
            break


def fix_row(row):
    for i in range(len(row)):
        for j in range(i, len(row)):
            nums = [row[i], row[j]]
            for rule in rules:
                if list(reversed(rule)) == nums:
                    row[i], row[j] = row[j], row[i]
                    break
    return row


for row in rows_to_fix:
    fixed_row = fix_row(row)
    result += int(fixed_row[len(row)//2])

print(result)


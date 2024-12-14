from pprint import pprint

with open('input1.txt') as file:
    rows = []
    for line in file.readlines():
        rows.append(list(line.strip()))


direction = (-1, 0)


def turn():
    while True:
        yield (0, 1)
        yield (1, 0)
        yield (0, -1)
        yield (-1, 0)


turn_gen = turn()


guard_i, guard_j = -1, -1
for i in range(len(rows)):
    for j in range(len(rows[i])):
        if rows[i][j] == '^':
            guard_i, guard_j = i, j


while True:
    # guard move
    new_i, new_j = guard_i + direction[0], guard_j + direction[1]
    if (new_i < 0 or new_j < 0
        or new_i >= len(rows) or new_j >= len(rows[0])):
        rows[guard_i][guard_j] = 'X'
        break
    if rows[new_i][new_j] == '#':
        direction = next(turn_gen)
        continue
    rows[guard_i][guard_j] = 'X'
    guard_i, guard_j = new_i, new_j


count = 0
for row in rows:
    for i in row:
        count += i == 'X'

print(count)


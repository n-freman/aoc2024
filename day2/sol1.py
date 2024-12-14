with open('input1.txt') as file:
    lines = file.readlines()


arr = []
for line in lines:
    arr.append(list(map(int, line.strip().split())))

count = 0

for row in arr:
    inc_dec = []
    for i in range(1, len(row)):
        diff = row[i] - row[i-1]
        if not 1 <= abs(diff) <= 3:
            break
        inc_dec.append(diff > 0)
    else:
        print(inc_dec)
        if all(inc_dec) or not any(inc_dec):
            count += 1

print(count)


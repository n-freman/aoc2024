from itertools import product

from tqdm import tqdm

with open('input1.txt') as file:
    lines = file.readlines()

possible_signs = ['||', '*', '+']
rows = {}
for line in lines:
    key, values = line.split(': ')
    rows[int(key)] = list(map(int, values.strip().split()))


def check_line(result, values) -> bool:
    products = list(product(*[possible_signs for i in range(len(values)-1)]))
    for i in tqdm(range(len(products)), leave=False):
        if join(values, products[i]) == result:
            return True
    return False


def join(numbers, signs):
    current = numbers[0]
    for i in range(len(signs)):
        if signs[i] == '||':
            current = eval(f'{current}{numbers[i+1]}')
        else:
            current = eval(f'{current}{signs[i]}{numbers[i+1]}')
    return current


count = 0
for key, values in tqdm(rows.items()):
    if check_line(key, values):
        count += key
print(count)

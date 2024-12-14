from itertools import product

with open('input1.txt') as file:
    lines = file.readlines()

possible_signs = ['*', '+']
rows = {}
for line in lines:
    key, values = line.split(': ')
    rows[int(key)] = list(map(int, values.strip().split()))


def check_line(result, values) -> bool:
    products = list(product(*[possible_signs for i in range(len(values)-1)]))
    for i in range(len(products)):
        if join(values, products[i]) == result:
            return True
    return False


# def binary_search(values, products, result) -> bool:
#     start = 0
#     end = len(products)
#     while True:
#         mid = (start + end) // 2
#         prod_value = join(values, products[mid])
#         if prod_value == result:
#             return True
#         if start == end or abs(start - end) == 1:
#             return False
#         if prod_value > result:
#             start = mid
#         else:
#             end = mid
# 

def join(numbers, signs):
    current = numbers[0]
    for i in range(len(signs)):
        current = eval(f'{current}{signs[i]}{numbers[i+1]}')
    return current


count = 0
for key, values in rows.items():
    if check_line(key, values):
        count += key
print(count)

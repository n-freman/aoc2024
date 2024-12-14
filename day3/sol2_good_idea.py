import regex

# pattern = re.compile(r'mul\((\d{1,3}),(\d+)\)')
# 
# lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
# 
# with open('input1.txt') as file:
#     lines = file.readlines()
# 
# total = 0
# 
# filtered_memory = []
# for line in lines:
#     for element in line.split('do()'):
#         filtered_memory.append(element.split('don\'t()')[0])
# 
# for line in filtered_memory:
#     nums = pattern.findall(line)
#     for x, y in nums:
#         print(x, y)
#         total += int(x) * int(y)
# 
# print(total)

def read_input(input_file_dir):
    with open(input_file_dir, 'r') as file:
        lines = file.readlines()
    return lines


def sum_multiplications(memory):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    total = 0
    for element in memory:
        multiplications = regex.findall(pattern, element)
        print(multiplications)
        for x, y in multiplications:
            print('adding')
            total += int(x) * int (y)
    return total


def remove_inactive_memory(memory):
    filtered_memory = list()
    for element in memory:
        for e in element.split("do()"):
            filtered_memory.append(e.split("don't(")[0])
    return filtered_memory


def sum_multiplications_activation(memory):
    memory = remove_inactive_memory(memory)
    return sum_multiplications(memory)


input = read_input("./input1.txt")
print(sum_multiplications_activation(input))


import re

pattern = re.compile(r'mul\(\d+,\d+\)')

# text = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'


with open('input1.txt') as file:
    lines = file.readlines()

total = 0

def process(text):
    text = text[4:-1]
    nums = text.split(',')
    print(nums)
    return int(nums[0]) * int(nums[1])


for line in lines:
    for match in pattern.findall(line):
        total += process(match)
print(total)


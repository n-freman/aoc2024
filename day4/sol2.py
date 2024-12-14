with open('input1.txt') as file:
    lines = file.readlines()

letters = []

for i in range(len(lines)):
    letters.append(list(lines[i].strip()))

search_patterns = [
    [
        ['M', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'S'],
    ],
    [
        ['S', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'M'],
    ],
    [
        ['S', '.', 'M'],
        ['.', 'A', '.'],
        ['S', '.', 'M'],
    ],
    [
        ['M', '.', 'M'],
        ['.', 'A', '.'],
        ['S', '.', 'S'],
    ]    
]


count = 0


def preprocess_section(section):
    section[0][1] = '.'
    section[1][0] = '.'
    section[1][2] = '.'
    section[2][1] = '.'
    return section


for i in range(2, len(letters)):
    for j in range(2, len(letters[0])):
        section = []
        for i_ in range(i-2, i+1):
            section_row = []
            for j_ in range(j-2, j+1):
                section_row.append(letters[i_][j_])
            section.append(section_row)
        section = preprocess_section(section)
        for pattern in search_patterns:
            if section == pattern:
                count += 1
                break

print(count)


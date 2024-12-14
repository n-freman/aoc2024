from pprint import pprint

with open('input1.txt') as file:
    lines = file.readlines()

word_to_search = 'XMAS'
letters = []

for i in range(len(lines)):
    letters.append(list(lines[i].strip()))

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]
row_count = len(letters)
col_count = len(letters[0])


def search_for_xmax(row, col, direction, word) -> bool:
    if word == word_to_search:
        return True
    new_row = row + direction[0]
    new_col = col + direction[1]
    if new_row >= row_count or new_col >= col_count:
        return False
    if new_row < 0 or new_col < 0:
        return False
    if word_to_search[:len(word)] != word:
        return False
    return search_for_xmax(new_row,
                           new_col,
                           direction,
                           word+letters[new_row][new_col])


final_look = [['.' for i in range(col_count)] for j in range(row_count)]
count = 0
for row in range(row_count):
    for col in range(col_count):
        for direction in directions:
            count += search_for_xmax(row,
                                     col,
                                     direction,
                                     letters[row][col])
    #     if col == 5 and row == 0:
    #         break
    # if col == 5 and row == 0:
    #     break

print(count)

from pprint import pprint
from copy import deepcopy

with open('input1.txt') as file:
    rows = []
    for line in file.readlines():
        rows.append(list(line.strip()))


def turn():
    while True:
        yield (0, 1)
        yield (1, 0)
        yield (0, -1)
        yield (-1, 0)




def check_board(board):
    cell_count = len(board) * len(board[1])
    turn_gen = turn()
    direction = (-1, 0)
    guard_i, guard_j = -1, -1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if rows[i][j] == '^':
                guard_i, guard_j = i, j
    
    move_count = 0    
    while True:
        if move_count >= cell_count:
            return True
        # guard move
        new_i, new_j = guard_i + direction[0], guard_j + direction[1]
        if (new_i < 0 or new_j < 0
            or new_i >= len(board) or new_j >= len(board[0])):
            board[guard_i][guard_j] = 'X'
            break
        if board[new_i][new_j] in ['#', 'O']:
            direction = next(turn_gen)
            continue
        guard_i, guard_j = new_i, new_j
        move_count += 1
    
    return False    


option_count = 0

for i in range(len(rows)):
    for j in range(len(rows[i])):
        print(f'Checking cell {i}x{j}')
        if rows[i][j] in ['#', '^']:
            continue
        new_board = deepcopy(rows)
        new_board[i][j] = 'O'
        option_count += check_board(new_board)

print(option_count)


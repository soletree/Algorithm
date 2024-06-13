import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
board_flip = []
row_cnt = 0
col_cnt = 0

for j in range(n):
    flip_row = []
    for i in range(n):
        flip_row.append(board[i][j])
    board_flip.append(flip_row)

for row in board:
    word = ''.join(row)
    for replaced_word in word.replace('X', ' ').split():
        if len(replaced_word) > 1:
            row_cnt += 1

for row in board_flip:
    word = ''.join(row)
    for replaced_word in word.replace('X', ' ').split():
        if len(replaced_word) > 1:
            col_cnt += 1
        
print(row_cnt, col_cnt)
import sys
import copy
from collections import *
input = sys.stdin.readline

def solve(x, y, color, board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    board[x][y] = ''
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue
            if board[nx][ny] == '':
                continue

            if board[nx][ny] not in color:
                continue
            
            board[nx][ny] = ''
            q.append((nx, ny))


n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
rg_board = copy.deepcopy(board)
r = 0
g = 0
b = 0
rg = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == '':
            continue
        if board[i][j] == 'R':
            solve(i, j, 'R', board)
            r += 1
        elif board[i][j] == 'G':
            solve(i, j, 'G', board)
            g += 1
        elif board[i][j] == 'B':
            solve(i, j, 'B', board)
            b += 1

for i in range(n):
    for j in range(n):
        if rg_board[i][j] == '':
            continue
        if rg_board[i][j] == 'B':
            continue
        
        if rg_board[i][j] == 'R' or rg_board[i][j] == 'G':
            solve(i, j, 'RG', rg_board)
            rg += 1

print(r+g+b, rg+b)
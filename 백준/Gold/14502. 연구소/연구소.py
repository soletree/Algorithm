import sys
from itertools import *
from copy import *
from collections import *
input = sys.stdin.readline

def simulate(board, start, wall):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    for s in start:
        q.append(s)

    for w in wall:
        board[w[0]][w[1]] = 1

    cnt = 0 

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            if board[nx][ny] > 0 :
                continue

            if board[nx][ny] == -1:
                continue

            board[nx][ny] = -1
            cnt += 1

            q.append((nx,ny))
            

    return cnt

n, m = map(int, input().split())
board = []
start = set()
wall = set()
# 이미 세워진 벽은 조합에 포함하지 않도록
coor = set()
ans = 0

for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(m):
        coor.add((i,j))
        if row[j] == 2:
            start.add((i,j))
        if row[j] == 1:
            wall.add((i,j))

start_cnt = len(start) + len(wall)
for c in combinations(coor-wall-start, 3):
    new_board = deepcopy(board)
    ans = max(n*m - simulate(new_board, start, c) - start_cnt -3, ans)
print(ans)
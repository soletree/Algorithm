import sys
from collections import *
input = sys.stdin.readline

def solve(start, end, n):
    board = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((start[0], start[1], 0))
    
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    
    if start == end:
        return 0
    
    while q:
        x, y, cnt = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            if board[nx][ny]:
                continue

            if (nx, ny) == end:
                return cnt+1

            board[nx][ny] = True
            q.append((nx,ny, cnt+1))           
            

t = int(input())

for _ in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    print(solve(start, end, n))
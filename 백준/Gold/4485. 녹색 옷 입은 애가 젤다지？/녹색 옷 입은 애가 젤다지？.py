import sys
from heapq import *
input = sys.stdin.readline

def solve(board, n):
    visited = [[False for _ in range(n)] for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = []
    heappush(q, (board[0][0],0,0))
    ans = 0
    while q:
        cost, x, y = heappop(q)

        if visited[x][y]:
            continue
    
        visited[x][y] = True
        
        if (x, y) == (n-1, n-1):
            ans = cost
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            if visited[nx][ny]:
                continue

            heappush(q, (cost + board[nx][ny], nx, ny))

    return ans

t = 0
while True:
    t += 1
    n = int(input())
    
    if n == 0:
        break
    
    board = [list(map(int, input().split())) for _ in range(n)]
    print(f'Problem {t}: {solve(board, n)}')
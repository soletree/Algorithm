#2589
import sys
from collections import *
input = sys.stdin.readline
INF = int(1e9)

def solve(x, y):
    global ans
    dx = [1, -1, 0, 0]
    dy = [0, 0 , 1, -1]
    visited = [[INF for _ in range(w)] for _ in range(l)]
    
    if board[x][y] =='W':
        return 

    visited[x][y] = 0
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # out of index
            if nx < 0 or nx >= l or ny < 0 or ny >= w:
                continue
            
            # 바다는 방문하지 않음
            if board[nx][ny] == 'W':
                continue
            
            # 처음 방문하는 경우 
            if visited[nx][ny] == INF:
                q.append((nx, ny))
                
            visited[nx][ny] = min(visited[x][y] + 1, visited[nx][ny])
            ans = max(ans, visited[nx][ny])

l, w = map(int, input().split())
board = [list(input().rstrip()) for _ in range(l)]
ans = 0

for i in range(l):
    for j in range(w):
        solve(i, j)
        
print(ans)
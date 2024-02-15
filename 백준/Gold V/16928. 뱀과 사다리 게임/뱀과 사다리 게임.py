import sys
from collections import *
input = sys.stdin.readline

def solve():
    global ans, visited
    q = deque()
    visited[1] = True
    q.append((1,0))
    
    while q:
        curr, cnt = q.popleft()
        
        for i in range(1, 7):
            next = curr + i
            
            if next > 100:
                break

            if next == 100:
                ans = min(ans, cnt+1)
                return

            if visited[next]:
                continue

            if board[next] != 0:
                next = board[next]

            visited[next] = True
            q.append((next, cnt+1))
            

n, m = map(int, input().split())
board = [0] * 101
visited = [False] * 101

for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    board[u] = v

ans = int(1e9)
solve()
print(ans)
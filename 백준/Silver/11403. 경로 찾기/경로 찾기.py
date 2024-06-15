import sys
from collections import *
input = sys.stdin.readline

def traversal(v):    
    q = deque()
    q.append(v)
    
    visited = [False] * n
    
    while q:
        curr = q.popleft()
            
        for next in range(n):
            if visited[next]:
                continue
            
            if adj[curr][next] == 0:
                continue

            result[v][next] = 1
            result[curr][next] = 1
            visited[next] = True
            q.append(next)
            
n = int(input())

adj = [list(map(int, input().split())) for _ in range(n)]
result = [[0 for _ in range(n)] for _ in range(n)]

for v in range(n):
    traversal(v)
    
for i in range(n):
    print(*result[i])
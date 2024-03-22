import sys
from collections import *
input = sys.stdin.readline

def bfs(start):
    visited = [0] * (n+1)
    q = deque()
    q.append(start)
    cnt = 0
    
    while q:
        v = q.popleft()
        
        if visited[v] == 0:
            cnt += 1
            visited[v] = cnt
        else:
            continue

        for next in sorted(adj[v]):
            if visited[next] != 0:
                continue
            
            q.append(next)
    
    print(*visited[1:], sep='\n')
        

n, m, r = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for sub in adj:
    sub.sort()
    
bfs(r)
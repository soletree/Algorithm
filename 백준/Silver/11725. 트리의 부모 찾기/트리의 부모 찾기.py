import sys
from collections import *
input = sys.stdin.readline

def bfs(start, adj, visited):
    global ans
    q = deque([start])
    visited[start] = True
    
    while q:
        vertex = q.popleft()
        for next in adj[vertex]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                ans[next] = vertex
    



n = int(input())

visited = [False] * (n+1)
adj = [[] for _ in range(n+1)]
ans = [-1] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


bfs(1, adj, visited)
print(*ans[2:], sep='\n')
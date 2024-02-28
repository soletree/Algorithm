import sys
from heapq import *
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())
adj = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int ,input().split())
    adj[start][end] = min(adj[start][end], cost)


start, end = map(int, input().split())
visited = [False] * (n+1)
q = []
heappush(q, (0, start, [start]))
dist = [INF] * (n+1)
ans = []

while q:
    cost, v, path = heappop(q)
    
    if visited[v]:
        continue
    
    visited[v] = True
    dist[v] = cost

    if v == end:
        ans = path
        break 
    
    for next in range(1, n+1):
        if visited[next]:
            continue

        if dist[next] < cost + adj[v][next]:
            continue
        
        new_path = path + [next]
        heappush(q, (cost + adj[v][next], next, new_path))

print(dist[end])
print(len(ans))
print(*ans, sep=' ')
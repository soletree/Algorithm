import sys
from collections import *
from heapq import *
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
costs = [[INF if i!=j else 0 for i in range(n)] for j in range(n)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    costs[start-1][end-1] = min(cost, costs[start-1][end-1])

start, end = map(int, input().split())

dist = [INF for _ in range(n)]
visited = [False] * n

q = []
heappush(q, (0, start-1))

while q:
    cost, v = heappop(q)
    
    if visited[v]:
        continue
    
    dist[v] = cost
    visited[v] = True

    if v == end-1:
        break
    
    for next in range(n):
        if costs[v][next] == INF:
            continue
        
        if visited[next]:
            continue
        
        if dist[next] < costs[v][next]+cost:
            continue
        
        heappush(q, (costs[v][next]+cost, next))

print(dist[end-1])
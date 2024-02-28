import sys
from heapq import *
input = sys.stdin.readline

INF = int(1e9)
n,m,k,x = map(int, input().split())
adj = [[] for _ in range(n)]
dists = [INF] * n
visited = [False] * n
for _ in range(m):
    start, end = map(int, input().split())
    adj[start-1].append(end-1)

q = []
heappush(q, (0, x-1))
flag = True
while q:
    cost, v = heappop(q)

    if visited[v]:
        continue
    
    dists[v] = cost
    visited[v] = True

    if cost == k:
        print(v+1)
        flag = False

    if cost > k:
        break

    for next in adj[v]:
        if visited[next]:
            continue

        if dists[next] < cost+1:
            continue
        
        heappush(q, (cost+1, next))


if flag:
    print(-1)
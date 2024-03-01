import sys
from collections import *
input = sys.stdin.readline

def solve(start):
    visited = [-1] * (n+1)
    visited[start] = 0
    
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        for next in adj[v]:
            if visited[next] != -1:
                continue

            visited[next] = visited[v] + 1
            q.append(next)

    return sum(visited[1:])
    

n, m = map(int ,input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

ans = 0
min_cnt = n * n
for i in range(1, n+1):
    cnt = solve(i)
    if cnt < min_cnt:
        ans = i
        min_cnt = cnt

print(ans)
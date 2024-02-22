import sys
from collections import *
input = sys.stdin.readline

n = int(input())
adj = [[]]
t = [-1] * (n+1)
for _ in range(n):
    adj.append(list(map(int, input().split())))

m = int(input())
first = list(map(int, input().split()))
q = deque()
rumor_cnt = [0] * (n+1)

for f in first:
    q.append(f)
    t[f] = 0

while q:
    curr = q.popleft()

    for next in adj[curr][:-1]:
        rumor_cnt[next] += 1
    
    for next in adj[curr][:-1]:
        # 이미 루머를 믿고 있는 경우 다음 방문 때 포함하지 않음 
        if t[next] > -1:
            continue

        if not adj[next][:-1]:
            continue

        if rumor_cnt[next] / len(adj[next][:-1]) < 0.5:
            continue
        
        q.append(next)
        t[next] = t[curr] + 1  

print(*t[1:], sep=' ')
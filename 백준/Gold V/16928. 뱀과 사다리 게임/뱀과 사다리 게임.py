import sys
from collections import *
input = sys.stdin.readline

def solve():
    global ans, dp
    q = deque()
    dp[1] = 0
    q.append((1,0))
    
    while q:
        curr, cnt = q.popleft()
        
        for i in range(1, 7):
            next = curr + i
            
            if next > 100:
                break

            if next == 100:
                dp[next] = min(dp[next], cnt+1)
                return

            if dp[next] < cnt+1:
                continue

            if snakes[next] != 0:
                next = snakes[next]
            
            if ladders[next] != 0:
                next = ladders[next]

            dp[next] = min(dp[next], cnt+1)
            q.append((next, cnt+1))
            

n, m = map(int, input().split())
ladders = [0] * 101
snakes = [0] * 101
dp = [int(1e9)] * 101

for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snakes[u] = v

ans = int(1e9)
solve()
print(dp[100])
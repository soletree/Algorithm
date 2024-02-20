n = int(input())
cost = [[]]
dp = [0] * 16

for _ in range(n):
    cost.append(list(map(int, input().split())))
    
for i in range(1, n+1):
    dp[i] = cost[i][1]

for i in range(1, n+1):
    t, p = cost[i]
    
    if i+t-1 > n:
        dp[i] = 0
        continue
    
    for j in range(i+t, n+1):
        dp[j] = max(dp[j], dp[i] + cost[j][1])

print(max(dp))
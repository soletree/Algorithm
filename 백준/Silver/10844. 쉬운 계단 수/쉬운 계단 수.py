n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(0, 10):
        if j-1 >= 0:
            dp[i][j] += dp[i-1][j-1]
        if j+1 <= 9:
            dp[i][j] += dp[i-1][j+1]
            
print(sum(dp[n]) % 1_000_000_000)
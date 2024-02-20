def solve(a, b, c):
    global dp
    if a<=0 or b<=0 or c<=0:
        return dp[0][0][0]

    if a>20 or b>20 or c>20:
        return dp[20][20][20]
    if a<b and b<c:
        return dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
    return dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]


dp = [[[0 for _ in range(21)] for _ in range(21) ] for _ in range(21)]
dp[0][0][0] = 1

for i in range(21):
    for j in range(21):
        for k in range(21):
            dp[i][j][k] = solve(i, j, k)

while True:
    a, b, c = map(int, input().split())
    if (a,b,c) == (-1,-1,-1):
        break

    ans = solve(a, b, c)
    print(f'w({a}, {b}, {c}) = {ans}')
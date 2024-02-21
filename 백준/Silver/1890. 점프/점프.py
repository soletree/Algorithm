import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

down = (1, 0)
right = (0, 1)

for dx, dy in (down, right):
    nx = 0 + dx * board[0][0]
    ny = 0 + dy * board[0][0]
    
    if nx > n-1 or ny > n-1:
        continue
    
    dp[nx][ny] = 1


for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue

        if i == n-1 and j == n-1:
            continue
        
        if dp[i][j] == 0:
            continue
        
        for dx, dy in (down, right):
            nx = i + dx * board[i][j]
            ny = j + dy * board[i][j]
            
            if nx > n-1 or ny > n-1:
                continue
            
            dp[nx][ny] += dp[i][j]
   
print(dp[n-1][n-1])
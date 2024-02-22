def solve(x, y, cnt):
    global ans
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    ans = max(ans, cnt)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx > r-1 or ny < 0 or ny > c-1:
            continue

        
        if visited[ord(board[nx][ny])-65]:
            continue

        visited[ord(board[nx][ny])-65] = True
        solve(nx, ny, cnt+1)
        visited[ord(board[nx][ny])-65] = False

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [False] * 26
ans = 0

solve(-1,0,0)
print(ans)
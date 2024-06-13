SIZE = 100
board = [[0 for _ in range(SIZE+1)] for _ in range(SIZE+1)]

#왼쪽 아래 꼭짓점 (x, y)- 오른쪽 위 꼭짓점 (x,y)
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] += 1
    

cnt = 0
for i in range(1, SIZE+1):
    for j in range(1, SIZE+1):
        if board[i][j] > 0:
            cnt += 1

print(cnt)
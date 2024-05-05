board = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

result = 0
for row in board:
    for col in row:
        if col == 1:
            result += 1


print(result)
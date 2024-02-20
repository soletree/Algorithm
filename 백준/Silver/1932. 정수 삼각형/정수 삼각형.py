n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))


for i in range(1, n):
    for j in range(0, i+1):
        if j-1 < 0:
            triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            continue

        if j == i:
            triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            continue
        
        triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]

print(max(triangle[n-1]))
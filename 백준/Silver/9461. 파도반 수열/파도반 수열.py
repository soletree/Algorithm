t = int(input())
SIZE = 100
p = [0 for _ in range(SIZE + 1)]
p[1], p[2], p[3] = 1, 1, 1

for i in range(4, SIZE+1):
    p[i] = p[i-3]+p[i-2]

for _ in range(t):
    n = int(input())
    print(p[n])
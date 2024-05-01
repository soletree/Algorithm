p1 = tuple(map(int, input().split()))
p2 = tuple(map(int, input().split()))
p3 = tuple(map(int, input().split()))

a = (p1[0]-p2[0], p1[1]-p2[1])
b = (p2[0]-p3[0], p2[1]-p3[1])
z = a[0] * b[1] - a[1] * b[0]

if z == 0:
    print(0)
elif z > 0:
    print(1)
else:
    print(-1)
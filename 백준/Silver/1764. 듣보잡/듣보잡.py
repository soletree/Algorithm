import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = set()
see = set()

for _ in range(n):
    listen.add(input().rstrip())

for _ in range(m):
    see.add(input().rstrip())

print(len(listen & see))
print(*sorted(listen & see), sep='\n')
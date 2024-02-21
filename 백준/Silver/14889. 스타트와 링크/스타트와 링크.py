from itertools import *

def capacity(c):
    result = 0
    for i, j in combinations(c, 2):
        result += s[i][j] + s[j][i]

    return result

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)

people = [i for i in range(n)]


for p in combinations(people, n//2):
    start = p
    link = []
    for i in range(n):
        if i in p:
            continue
        link.append(i)
     
    ans = min(ans, abs(capacity(start)-capacity(link)))

print(ans)
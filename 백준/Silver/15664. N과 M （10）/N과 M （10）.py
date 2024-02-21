def solve(i, arr):
    if len(arr) == m:
        ans.add(tuple(arr))
        return

    for next in range(i, n):
        if visited[next]:
            continue

        visited[next] = True
        arr.append(num[next])
        
        solve(next, arr)
        
        arr.pop()
        visited[next] = False

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = set()
visited = [False] * n

solve(0, [])

for row in sorted(ans):
    print(*row, sep = ' ')
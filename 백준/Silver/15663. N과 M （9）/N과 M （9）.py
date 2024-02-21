def solve(arr):
    if len(arr) == m:
        ans.add(tuple(arr))
        return

    for next in range(n):
        if visited[next]:
            continue

        visited[next] = True
        arr.append(num[next])
        solve(arr)
        arr.pop()
        visited[next] = False

        
n, m = map(int, input().split())
visited = [False] * n
num = list(map(int, input().split()))
ans = set()

solve([])

for col in sorted(ans):
    print(*col, sep=' ')
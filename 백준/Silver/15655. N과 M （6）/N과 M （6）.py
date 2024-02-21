def solve(i, ans):
    if len(ans) == m:
        print(*ans, sep = ' ')
        ans = []
        return
    for next in range(i+1, n):
        if visited[next]:
            continue

        visited[next] = True
        ans.append(num[next])
        solve(next, ans)
        visited[next] = False
        ans.pop()
    

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = [False] * n
ans = []
solve(-1, [])
def solve(first, n, m, cnt, arr):
    global visited
    if len(arr) == m:
        print(*arr, sep = ' ')
        arr = []
        return
    
    for i in range(1, n+1):
        if first == i:
            continue
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        solve(i, n, m, cnt+1, arr)
        arr.pop()
        visited[i] = False
    
n, m = map(int, input().split())
visited = [False] * (n+1)
arr = []
for i in range(1, n+1):
    visited[i] = True
    solve(i, n, m, 1, [i])
    visited[i] = False
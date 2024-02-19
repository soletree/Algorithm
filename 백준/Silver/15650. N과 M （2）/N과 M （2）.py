def solve(v, arr):
    global n, m, visited
    if len(arr) == m:
        print(*arr, end = ' ')
        print()
        return
    for next in range(v+1, n+1):
        if visited[next]:
            continue
        
        visited[next] = True
        arr.append(next)
        solve(next, arr)
        arr.pop()
        visited[next] = False
        

n, m = map(int, input().split())
visited = [False] * (n+1)
solve(0, [])
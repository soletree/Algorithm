def solve(v, arr):
    global n, m
    if len(arr) == m:
        print(*arr, end = ' ')
        print()
        return
    for next in range(v, n+1):
        arr.append(next)
        solve(next, arr)
        arr.pop()

n, m = map(int, input().split())
solve(1, [])
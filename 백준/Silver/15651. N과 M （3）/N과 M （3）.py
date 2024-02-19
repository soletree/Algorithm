def solve(arr):
    global n, m

    if len(arr) == m:
        print(*arr, end = ' ')
        print()
        return

    for next in range(1, n+1):
        arr.append(next)
        solve(arr)
        arr.pop()
    

n, m = map(int, input().split())
solve([])
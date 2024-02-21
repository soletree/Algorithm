def solve(v, arr):
    if len(arr) == m:
        print(*arr, sep = ' ')
        return 

    for next in range(v, n):
        arr.append(num[next])
        solve(next, arr)
        arr.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
solve(0, [])
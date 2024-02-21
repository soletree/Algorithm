def solve(i, arr):
    if len(arr) == m:
        print(*arr, sep=' ')
        return

    for next in range(i, len_num):
        arr.append(num[next])
        solve(next, arr)
        arr.pop()

n, m = map(int, input().split())
num = list(set(map(int, input().split())))
num.sort()
len_num = len(num)

solve(0, [])
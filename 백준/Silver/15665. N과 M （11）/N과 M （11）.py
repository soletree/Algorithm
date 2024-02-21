def solve(arr):
    if len(arr) == m:
        print(*arr, sep=' ')
        return

    for next in range(len_num):
        arr.append(num[next])
        solve(arr)
        arr.pop()


n, m = map(int, input().split())
num = sorted(set(list(map(int, input().split()))))
len_num = len(num)

solve([])
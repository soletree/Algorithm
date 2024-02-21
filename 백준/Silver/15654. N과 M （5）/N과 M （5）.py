def solve(arr):
    if len(arr) == m:
        print(*arr, sep = ' ')
        return 

    for next in range(n):
        if visited[next]:
            continue

        visited[next] = True
        arr.append(num[next])

        solve(arr)
        
        visited[next] = False
        arr.pop()      
        
visited = [False] * 9
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
solve([])
def back(to, cost, cnt):
    global ans, visited, n, costs
    
    if cnt == n:
        if costs[to][0] == 0:
            return
        ans = min(ans, cost+costs[to][start])
        return

    for i in range(n):
        if to == i:
            continue
        if visited[i]:
            continue
       
        if costs[to][i] == 0:
            continue
        
        visited[i] = True
        back(i, cost + costs[to][i], cnt+1)
        visited[i] = False   


n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
ans = 1_000_000 * 10
start = 0

visited[start] = True
back(0, 0, 1)
print(ans)
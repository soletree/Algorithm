def solve(i, arr, vowel_cnt, con_cnt):
    if len(arr) == l:
        if vowel_cnt < 1:
            return

        if con_cnt < 2:
            return 
        
        print(*arr, sep='')
        return

    for next in range(i+1, c):
        if visited[next]:
            continue

        visited[next] = True
        arr.append(chars[next])

        if chars[next] in ['a', 'e', 'i', 'o', 'u']:
            solve(next, arr, vowel_cnt+1, con_cnt)
        else:
            solve(next, arr, vowel_cnt, con_cnt+1)
        arr.pop()
        visited[next] = False

l, c = map(int, input().split())
chars = list(input().split())
chars.sort()
visited = [False] * c

solve(-1, [], 0, 0)
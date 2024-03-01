from collections import *

a, b = map(int, input().split())

q = deque()
q.append((a, 0))
ans = -1
while q:
    v, cnt = q.popleft()
    
    if v == b:
        ans = cnt
        break
    
    if v * 2 <= b:
        q.append((v*2, cnt+1))

    if int(str(v)+'1') <= b:
        q.append((int(str(v)+'1'), cnt+1))

print(ans+1 if ans != -1 else ans)
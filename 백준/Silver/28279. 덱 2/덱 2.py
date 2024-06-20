from collections import *
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    cmd = list(map(int, input().split()))
    command = cmd[0]
    if command == 1:
        q.appendleft(cmd[1])
    if command == 2:
        q.append(cmd[1])
    if command == 3:
        if not q:
            print(-1)
            continue
        print(q.popleft())
    if command == 4:
        if not q:
            print(-1)
            continue
        print(q.pop())
    if command == 5:
        print(len(q))
    if command == 6:
        print(1 if len(q) == 0 else 0)
    if command == 7:
        if not q:
            print(-1)
            continue
        print(q[0])
    if command == 8:
        if not q:
            print(-1)
            continue
        print(q[-1])        
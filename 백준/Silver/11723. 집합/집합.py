import sys
input = sys.stdin.readline

m = int(input())
num = [False] * 21
all = [True] * 21
empty = [False] * 21
for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'add':
        num[int(cmd[1])] = True
    elif cmd[0] == 'remove':
        num[int(cmd[1])] = False
    elif cmd[0] == 'check':
        print(1 if num[int(cmd[1])] else 0)
    elif cmd[0] == 'toggle':
        num[int(cmd[1])] = not num[int(cmd[1])]
    elif cmd[0] == 'all':
        num = all[:]
    elif cmd[0] == 'empty':
        num = empty[:]
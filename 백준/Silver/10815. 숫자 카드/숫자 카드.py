n = int(input())
cards = set(list(map(int, input().split())))
m = int(input())
cmp = list(map(int, input().split()))

for i in cmp:
    if i in cards:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
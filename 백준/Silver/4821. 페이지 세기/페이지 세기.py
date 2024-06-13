while True:
    n = int(input())
    if n == 0:
        break

    page_set = set()
    pages = input().split(sep=',')

    for p in pages:
        bound = list(map(int, p.split(sep='-')))

        if len(bound) < 2:
            low, high = bound[0], bound[0]
        else:
            low, high = bound[0], bound[1]

        if high > n:
            high = n

        if low > high:
            continue
        
        for i in range(low,high+1):
            page_set.add(i)

    print(len(page_set))
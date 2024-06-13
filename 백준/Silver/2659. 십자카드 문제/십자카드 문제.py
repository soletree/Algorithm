def find_min_clock(num_list):
    result = [INF for _ in range(4)]
    for i in range(4):
        result = min(result, num_list[i:]+num_list[:i])
    return result


num = list(map(int, input().split()))
INF = int(1e9)
clock= find_min_clock(num)
clocks_set = set()

for i in range(1111, 10000):
    n = list(map(int, list(str(i))))
    #0은 시계수가 아님 
    if 0 in n:
        continue
    
    # 이미 체크한 수면 넘어감 
    if tuple(n) in clocks_set:
        continue

    n_clock = find_min_clock(n)
    if tuple(n_clock) in clocks_set:
        continue
    
    clocks_set.add(tuple(n_clock))

    if n_clock == clock:
        print(len(clocks_set))
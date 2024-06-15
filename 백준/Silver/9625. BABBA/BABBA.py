k = int(input())

result = [1, 0]
for _ in range(k):
    a_cnt = result[0]
    b_cnt = result[1]

    result[0] = b_cnt
    result[1] = a_cnt + b_cnt

print(*result, sep=' ')
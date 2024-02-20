n = int(input())
a, b, c = 1, 1, 1

for i in range(2, n+1):
    prev_a, prev_b, prev_c = a, b, c
    a = prev_b + prev_c
    b = prev_a + prev_c
    c = prev_a + prev_b + prev_c

print((a+b+c) % 9901)
# n: gear num, d: direction
def rotate_gear(n, d):
    # gear 1...4 -> index: gear-1 
    gear = gears[n-1]
    # 반시계
    if d == -1:
        result = gear[1:] + [gear[0]]
    else:
        result = [gear[-1]] + gear[0:-1]

    gears[n-1] = result

# 회전 여부 판단
# 더 작은 번호 f, 큰 번호 s
# True: 회전 함 
def cmp_gears(f, s):
    return gears[f-1][2] != gears[s-1][6]

def left_simulate(n, d):
    if n < 1:
        return
    
    if not cmp_gears(n, n+1):
        return

    left_simulate(n-1, -d)
    rotate_gear(n, d)
    

def right_simulate(n, d):
    if n > 4:
        return
    
    if not cmp_gears(n-1, n):
        return

    right_simulate(n+1, -d)
    rotate_gear(n, d)

    
gears = [list(input()) for _ in range(4)]
k = int(input())

for _ in range(k):
    # gear 1...4 -> index: gear-1
    gear_num, direct = map(int, input().split())
    left_simulate(gear_num-1, -direct)
    right_simulate(gear_num+1, -direct)
    rotate_gear(gear_num, direct)


ans = 0
for i in range(4):
    if gears[i][0] == '1':
        ans += 2 ** i

print(ans)
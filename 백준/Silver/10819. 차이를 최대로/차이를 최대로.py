from itertools import *

def calc_result(nums):
    result = 0
    for i in range(1, n):
        result += abs(nums[i]-nums[i-1])
    return result
    

n = int(input())
num = list(map(int, input().split()))
ans = 0

for p in permutations(num, n):
    ans = max(ans, calc_result(p))

print(ans)
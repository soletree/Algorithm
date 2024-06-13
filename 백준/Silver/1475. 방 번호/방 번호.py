room_num = input()
num_cnt = [0 for _ in range(0,10)]

# 각 자리 숫자가 나온 개수를 기록 
for digit in room_num:
    num_cnt[int(digit)] += 1

# 총 몇 세트가 필요한지 찾기
six_nine_sum = num_cnt[6]+num_cnt[9]
num_cnt[6] = int(six_nine_sum / 2)
num_cnt[9] = int((six_nine_sum+1)/2)

print(max(num_cnt))
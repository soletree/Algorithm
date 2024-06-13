# 다친 손가락
n = int(input())
# 셀 수 있는 횟수 
m = int(input())
# 다음 같은 수가 나올 때까지 셀수 있는 
finger = {1:[7], 2: [5,1], 3: [3], 4: [1,5], 5: [7]}

cnt = n-1
index = 0
finger_list = finger[n]
cnt_finger_list = len(finger_list)

if cnt_finger_list == 1:
    cnt += (finger_list[0]+1)*m
else:
    cnt += (finger_list[0]+1)* int(m/2+0.5) + (finger_list[1]+1)* int(m/2)

print(cnt)
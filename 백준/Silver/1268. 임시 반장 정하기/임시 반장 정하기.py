import sys
input = sys.stdin.readline

n = int(input())
student_list = []

ans = 1
max_cnt = 0

for _ in range(n):
    c_num = list(map(int, input().split()))
    student = set()
    
    for i in range(5):
        student.add((i+1, c_num[i]))

    student_list.append(student)


for i in range(n):
    s = student_list[i]
    cnt = 0
    
    for j in range(n):
        if i==j:
            continue
        if s & student_list[j]:
            cnt += 1

    if max_cnt < cnt:
        ans = i+1
        max_cnt = cnt
        
print(ans)
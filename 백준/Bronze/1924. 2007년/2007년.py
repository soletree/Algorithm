days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
x, y = map(int, input().split())
cnt = y - 1
for month in range(1, x):
    cnt += days[month]

print(weeks[cnt%7])
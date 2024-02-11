import sys
input=sys.stdin.readline

def solve(x,y):
    global cnt
    if x<0 or x>n-1 or y<0 or y>n-1:
        return False
    if houses[x][y]==1:
        cnt+=1
        houses[x][y]=0
        solve(x-1,y)
        solve(x,y-1)
        solve(x+1,y)
        solve(x,y+1)
        return True
    return False
        
n=int(input())
houses=[list(map(int,input().rstrip())) for _ in range(n)]
ans=[]
result=0
cnt=0
num=1
for i in range(n):
    for j in range(n):
        if solve(i,j):
            ans.append(cnt)
            result+=1
            cnt=0
            
print(result)
ans.sort()
print(*ans,sep='\n')
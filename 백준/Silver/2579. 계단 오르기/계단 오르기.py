import sys
input=sys.stdin.readline

def solve(n,stair):
    dp=[0]*(n+1)
    if n==1: return stair[1]
    elif n==2: return stair[1]+stair[2]
    
    dp[1]=stair[1]
    dp[2]=stair[1]+stair[2]

    for i in range(3,n+1):
        dp[i]=max(stair[i-1]+dp[i-3],dp[i-2])+stair[i]
        
    return dp[n]
    
n=int(input())
stair=[0]*(n+1)
for i in range(1,n+1): stair[i]=int(input())
print(solve(n,stair))
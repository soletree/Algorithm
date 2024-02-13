from collections import *



def bfs(maps):
    row = len(maps)
    col = len(maps[0])
    
    q = deque()
    q.append((0,0))
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    
    while q:
        x, y = q.popleft()
        for index in range(4):
            nx = x + dx[index]
            ny = y + dy[index]
            
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue 
            if maps[nx][ny] == 0:
                continue
            
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                continue
                
            maps[nx][ny] = min(maps[nx][ny], maps[x][y] + 1)
            
    return maps
            
def solution(maps):
    result = bfs(maps)
    
    return -1 if result[-1][-1] == 1 else result[-1][-1]
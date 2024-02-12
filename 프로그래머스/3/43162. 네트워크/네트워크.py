from collections import *

def bfs(vertex, visited, n, computers):
    if visited[vertex]:
        return False
     
    q = deque()
    q.append(vertex)
    visited[vertex] = True
    
    while q:
        # 인접 노드 순회 
        current = q.popleft()
        
        for index in range(n):
            # 자기 자신 무시
            if index == current:
                continue
            if computers[current][index] == 0:
                continue
            if visited[index]:
                continue
            q.append(index)
            visited[index] = True
            
    return True

def solution(n, computers):
    answer = 0
    computers = computers
    visited = [False] * n
    
    for vertex in range(n):
        if bfs(vertex, visited, n, computers):
            answer += 1
        
    
    return answer
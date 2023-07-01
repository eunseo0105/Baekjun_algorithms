from collections import deque

def bfs(start, visited, computers, n):
        queue = deque()
        queue.append(start)
        visited[start] = 1
        
        while queue:
            v = queue.popleft()
            for i in range(n):
                if computers[v][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    queue.append(i)
    
    
def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if visited[i] == 0:
            bfs(i, visited, computers, n)
            answer += 1
            
    return answer
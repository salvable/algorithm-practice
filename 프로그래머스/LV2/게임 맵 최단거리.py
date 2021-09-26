from collections import deque

def bfs(maps):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
    # 시작지점 1로 초기화
    visited[0][0] = 1
    
    q = deque([(0,0)])
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if visited[nx][ny] == -1 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    
    return visited[-1][-1]
    
def solution(maps):
    result = bfs(maps)
    
    return result

from collections import deque

def solution(n, edge): 
    graph = [[] for _ in range(n+1)]
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 방문노드 리스트, 1번은 시작지점이니 방문 처리
    visited = [0] * (n+1)
    visited[1] = 1
    
    #큐에 시작지점 1을 넣고 
    q = deque([1])
  
    while(q):
        n = q.popleft()
        for i in graph[n]:
            if visited[i]==0:
                q.append(i)
                visited[i] = visited[n]+1
            
    answer = visited.count(max(visited))
    
    return answer

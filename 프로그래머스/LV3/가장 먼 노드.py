from collections import deque

def solution(n, edge): 
    graph = [[] * (n+1) for i in range(n+1)]
    visit = [0] * (n+1)
    
    # 양방향
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    # 1번 노드 시작이므로 큐에 넣어줌
    q = deque([1])
    visit[1] = 1
    
    while q:
        node = q.popleft()
        
        for i in graph[node]:
            if visit[i] == 0:
                visit[i] = visit[node] + 1
                q.append(i)
                
    answer = visit.count(max(visit))
            
    
    return answer

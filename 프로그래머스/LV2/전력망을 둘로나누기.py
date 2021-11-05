def dfs(start, visit):
    global graph, count
    visit.append(start)
    count += 1
    for i in graph[start]:
        if i not in visit:
            dfs(i, visit)
    

def solution(n, wires):
    # 최댓값 설정
    global graph, count
    answer = []
    graph = [[] * (n+1) for _ in range(n+1)]
    
    # 양방향 연결
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)
        
    # 완성되어 있는 그래프에서 하나씩 빼서 확인 후 다시 넣어줌
    for x,y in wires:
        graph[x].remove(y)
        graph[y].remove(x)
        
        count = 0
        # 시작 노드와 방문노드 입력
        dfs(1,[])
        answer.append(abs(n - (count * 2)))
        
        graph[x].append(y)
        graph[y].append(x)
    
    return min(answer)

IINF = 1e9

def solution(n, results):
    answer = 0
    
    graph = [[INF] * (n+1) for _ in range(n+1)]

    
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                graph[i][j] = 0
    
    for i,j in results:
        graph[i][j] = 1
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
                
    for i in range(1,n+1):
        count = 0
        for j in range(1,n+1):
            if graph[i][j] != INF or graph[j][i] != INF:
                count +=1
        if count == n:
            answer += 1
    
    return answer

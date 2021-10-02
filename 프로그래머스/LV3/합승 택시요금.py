INF = int(1e9)

def solution(n, s, a, b, fares):
    graph = [[INF] * (n+1) for _ in range(n+1)]

    # 자기 자신으로 가는 거리는 0으로 초기화
    for i in range(n+1):
        graph[i][i] = 0
    

    for x,y,fee in fares:
        graph[x][y] = fee
        graph[y][x] = fee
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
                 
    answer = INF
    
    for i in range(1,n+1):
        answer = min(answer , graph[s][i] + graph[i][b] + graph[i][a])
    
    return answer

INF = int(1e9)

def pythonTest():
    n = 5
    m = 14

    graph = [[INF] * (n+1) for _ in range(n+1)]

    for a in range(n+1):
        for b in range(n+1):
            if a == b:
                graph[a][b] = 0

    arr = [[1,2,2],[1,3,3],[1,4,1],[1,5,10],[2,4,2],[3,4,1],[3,5,1],[4,5,3],[3,5,10],[3,1,8],[1,4,2],[5,1,7],[3,4,2],[5,2,4]]

    for i in arr:
        a, b, c = i[0],i[1],i[2]

        # 짧은 간선만 저장
        if c < graph[a][b]:
            graph[a][b] = c

    # k는 특정 지점을 거쳐가는 방법
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

    for a in range(1, n+1):
        for b in range(1,n+1):
            if graph[a][b] == INF:
                print(0, end=" ")
            else:
                print(graph[a][b], end=" ")
        print("\n")

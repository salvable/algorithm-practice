def pythonTest():

    # 노드의 개수 , 간선의 개수
    n,m = " "

    graph = [[INF] * (n+1) for _ in range(n+1)]

    for a in range(1,n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    arr = [[1,2],[1,3],[1,4],[2,4],[3,4],[3,5],[4,5]]

    for a,b in arr:
        # 서로 가는 비용은 1
        graph[a][b] = 1
        graph[b][a] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # x는 목적지 k 는 거쳐갈 번호
    x, k = " "

    distance = graph[1][k] + graph[k][x]

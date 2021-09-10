INF = int(1e9)

def pythonTest():
    n = 6

    graph = [[INF] * (n+1) for _ in range(n+1)]

    arr = [[1,5],[3,4],[4,2],[4,6],[5,2],[5,4]]

    for a in range(1,n+1):
        for b in range(1,n+1):
            if a == b:
                graph[a][b] = 0

    for i in arr:
        a, b = i[0], i[1]
        graph[a][b] = 1

    for i in graph[1:]:
        print(i[1:])
        print("\n")

    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

    for i in graph[1:]:
        print(i[1:])
        print("\n")

    result = 0

    for i in range(1,n+1):
        count = 0
        for j in range(1,n+1):
            if graph[i][j] != INF or graph[j][i] != INF:
                count += 1
        if count == n:
            result += 1

    print(result)

def pythonTest():
    n, m = 5, 7
    gragh = [[INF] * (n+1) for _ in range(n+1)]

    arr = [[1,2],[1,3],[1,4],[2,4],[3,4],[3,5],[4,5]]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                gragh[i][j] = 0

    for i, j in arr:
        gragh[i][j] = 1
        gragh[j][i] = 1

    # 거쳐갈 노트 x와 최종목적지 k
    x, k = 4, 5

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                gragh[i][j] = min(gragh[i][j], gragh[i][k] + gragh[k][j])

    # 1번 노드부터 k노드까지 간 횟수와 k 노드부터 x 노드까지 간 거리를 저장
    distance = gragh[1][k] + gragh[k][x]

    if distance >= INF:
        print("-1")
    else:
        print(distance)

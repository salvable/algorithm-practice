def pythonTest():
    #각각 도시갯수, 도로갯수, 거리정보, 출발도시정보
    n, m, k, x = 4,4,1,1
    arr = [[],[2,3],[3,4],[],[]]

    distance = [-1] * (n+1)
    distance[x] = 0

    q = deque([x])

    answer = []

    while(q):
        now = q.popleft()
        for node in arr[now]:
            # 그 노드가 방문하지 않은 지점이라면
            if distance[node] == -1:
                distance[node] = distance[now] + 1
                q.append(node)

    for i in range(len(distance)):
        if distance[i] == x:
            answer.append(i)

    if len(answer) == 0:
        print(-1)
    else:
        print(answer)

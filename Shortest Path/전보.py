def pythonTest():

    # 노드의 개수 , 간선의 개수 , 시작노드
    n, m, start = 3, 2, 1

    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    arr = [[1,2,4],[1,3,2]]

    # x로부터 y로 가는 거리 d
    for x,y,d in arr:
        graph[x].append((y,d))

    def dijkstra(start):
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0

        while q:
            dist, node = heapq.heappop(q)
            if distance[node] < dist:
                continue
            for i in graph[node]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))

    dijkstra(start)
    count = 0
    max_distance = 0

    for i in distance:
        if i != INF:
            count += 1
            max_distance = max(max_distance,i)

    # 시작노드는 뺴야하므로 -1
    print(count - 1,max_distance)

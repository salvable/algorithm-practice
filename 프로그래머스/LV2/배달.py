import heapq

INF = 1e9
                
def solution(N, road, K):
    
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    
    for a,b,c in road:
        # a는 시작지점 b는 도착지점 c 는 거리
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    def dijkstra(node):
        heap = []
        # 시작노드 0으로 초기화
        distance[node] = 0
        heapq.heappush(heap,(0,node))
        
        while heap:
            dist, now = heapq.heappop(heap)
            # 방문하였거나 최솟값이 아닌경우
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                # 거리가 기존거보다 짧은경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(heap,(cost,i[0]))
    
    dijkstra(1)
    
    answer = 0
    
    for i in distance:
        if i <= K:
            answer += 1
    
    return answer

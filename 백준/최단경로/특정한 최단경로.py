INF = int(1e9)
from collections import deque

import sys
import heapq

input = sys.stdin.readline


n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

# 무방향성이므로 둘다 기록
for _ in range(m):
    x, y, dist = map(int, input().split())
    graph[x].append((y,dist))
    graph[y].append((x,dist))

# 중간에 거칠 노드
node1, node2 = map(int, input().split())

def dijkstra(start,end):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    # 큐에 현재 거리와 시작노드를 넣어줌
    heapq.heappush(q,(0,start))

    while q:
        d, now = heapq.heappop(q)

        #처리된적이 있는경우
        if distance[now] < d:
            continue
        # 해당 그래프와 연결된 노드와 거리를 꺼냄
        for i in graph[now]:
            cost = d + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance[end]

result1 = dijkstra(1,node1) + dijkstra(node1,node2) + dijkstra(node2,n)
result2 = dijkstra(1,node2) + dijkstra(node2,node1) + dijkstra(node1,n)

answer = min(result1,result2)

if answer >= INF:
    print(-1)
else:
    print(answer)

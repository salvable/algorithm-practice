INF = int(1e9)
from collections import deque

import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, dist = map(int, input().split())
    graph[x].append((y,dist))

def dijkstra(start):
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

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

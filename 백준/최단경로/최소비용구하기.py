import heapq
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dijkstra(start):
    distance = [1e9] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, next_dist in graph[now]:
            cost = dist + next_dist

            # 다음 노드로 가는 코스트가 현재 저장되어 있던 코스트보다 작다면
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())

    graph[a].append((b, cost))

start, end = map(int, input().split())
result = dijkstra(start)

print(result[end])
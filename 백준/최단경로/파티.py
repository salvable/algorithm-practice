import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]


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


for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

answer = 0

for i in range(1, n + 1):
    target = dijkstra(i)
    home = dijkstra(x)

    answer = max(answer, target[x] + home[i])

print(answer)
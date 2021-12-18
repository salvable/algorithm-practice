from collections import deque
from sys import stdin
import sys

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    x, y, dist = map(int, input().split())
    graph[x].append((y, dist))
    graph[y].append((x, dist))

def bfs(start):

    q = deque()
    q.append(start)

    visited = [-1] * (n + 1)
    visited[start] = 0

    # 거리와 node값을 기록
    value = [0, 0]

    while q:
        node = q.popleft()

        for next_node, dist in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + dist
                q.append(next_node)
                if value[0] < visited[next_node]:
                    value = visited[next_node], next_node

    return value

dist, node = bfs(1)

dist, node = bfs(node)
print(dist)
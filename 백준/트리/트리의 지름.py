from collections import deque
from sys import stdin
import sys


v = int(input())

graph = [[] for _ in range(v + 1)]

for _ in range(v):
    arr = list(map(int, input().split()))
    for i in range(1,len(arr)-1,2):
        # arr[0]은 특정 노트 이후 2개씩은 연결된 노드와 가중치 정보
        graph[arr[0]].append((arr[i], arr[i+1]))

def bfs(start):
    q = deque()
    q.append(start)

    visited = [-1] * (v + 1)
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

# 루트에서 가장 먼 노드를 찾은 뒤에
dist, node = bfs(1)

# 다시한번 루트에서 가장 먼 노드에서  bfs를 돌려 제일 먼 노드, 거리를 찾음
dist, node = bfs(node)
print(dist)
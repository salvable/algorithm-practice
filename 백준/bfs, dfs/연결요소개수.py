from collections import deque
import sys
input = sys.stdin.readline

# 노드개수 n, 간선갯수 m
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
# 0번 인덱스는 안쓸거라 True
visited[0] = True

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()

        for next_node in graph[node]:
            # 방문하지 않은 경우에
            if visited[next_node] == False:
                # 방문표시와 큐에 추가
                visited[next_node] = True
                q.append(next_node)


answer = 0

for i in range(1, n + 1):
    # 이미 방문 했던 곳이라면
    if visited[i]:
        continue

    bfs(i)
    answer += 1

print(answer)

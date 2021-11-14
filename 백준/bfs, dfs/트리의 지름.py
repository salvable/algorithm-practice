from sys import stdin
from collections import deque

read = stdin.readline
V = int(read())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, read().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))

def bfs(start):
    visit = [-1] * (V + 1)
    que = deque()
    que.append(start)
    visit[start] = 0
    value = [0, 0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                que.append(e)
                if value[0] < visit[e]:
                    value = visit[e], e

    return value

# 1번 노드로 부터 가장 먼 노드를 구하고  
dist, node = bfs(1)

# 가장 멀리있는 노드로부터 가장 멀리있는 노드를 구한다.
dist, node = bfs(node)
print(dist)

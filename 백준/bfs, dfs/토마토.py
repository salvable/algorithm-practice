INF = int(1e9)
from collections import deque

m, n = map(int, input().split())
graph = []
q = deque([])
for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(m):  # 익은 토마토 큐에 저장
        if graph[i][j] == 1:
            q.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x,y = q.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

result = 0
flag = True
for g in graph:
    result = max(result, max(g))
    for i in g:
        if i == 0:
            flag = False
# 처음 토마토 값이 0일차에 1이므로 1을 뺴줌

if flag:
    print(result - 1)
else:
    print(-1)

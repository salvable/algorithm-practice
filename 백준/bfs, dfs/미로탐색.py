from collections import deque

from sys import stdin
N, M = map(int, stdin.readline().split())

graph = [stdin.readline().rstrip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 0,
q = deque()
q.append((0,0))
visited[0][0] = 1

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == "1" and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

print(visited[N-1][M-1])

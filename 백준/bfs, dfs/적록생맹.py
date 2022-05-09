from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [list(map(str, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                # 다음 좌표가 이전값과 같고 방문하지 않았을 경우 탐색
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True


for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i,j)
            answer += 1

print(answer, end= " ")

visited = [[False] * n for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        # 레드인거를 그린으로 다 바꿔줌
        if graph[i][j] == "R":
            graph[i][j] = "G"

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i,j)
            answer += 1

print(answer)
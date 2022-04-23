from collections import deque

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 넘어가면 패스
            if nx < 0 or nx > h + 1 or ny < 0 or ny > w + 1:
                continue
            # 벽이거나 방문한 경우 패스
            if visited[nx][ny] >= 0 or visited[nx][ny] == "*":
                continue
            # 그냥 길인 경우 먼저 처리  => 문을 열고 그 이후 행동보다 먼저 처리하기 위함
            if graph[nx][ny] == ".":
                visited[nx][ny] = visited[x][y]
                q.appendleft((nx, ny))
            # 문을 통하는 루트는 나중에 처리
            elif graph[nx][ny] == "#":
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return visited


for _ in range(int(input())):
    h, w = map(int, input().split())
    graph = []
    graph.append(list("." * (w + 2)))

    for _ in range(h):
        graph.append(list("." + input().strip() + "."))

    graph.append(list("." * (w + 2)))

    q = deque()

    for i in range(h + 2):
        for j in range(w + 2):
            # 수감자의 위치 기록
            if graph[i][j] == "$":
                graph[i][j] = "."
                q.append((i, j))

    x1, y1 = q.popleft()
    graph1 = bfs(x1, y1)
    x2, y2 = q.popleft()
    graph2 = bfs(x2, y2)
    graph3 = bfs(0, 0)

    answer = 1e9

    for i in range(h + 2):
        for j in range(w + 2):
            # 벽인 경우 패스
            if graph[i][j] == "*":
                continue

            if graph1[i][j] != -1 and graph2[i][j] != -1 and graph3[i][j] != -1:
                temp = graph1[i][j] + graph2[i][j] + graph3[i][j]
                # 그 값이 문이라면 3명으로 시작했으므로 중복으로 문을 연 횟수를 제외하기 위해 -2 해줌
                if graph[i][j] == "#":
                    temp -= 2

                answer = min(answer, temp)

    print(answer)
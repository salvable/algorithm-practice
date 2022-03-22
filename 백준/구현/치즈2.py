from collections import deque

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(8)]
second = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위안에 있고 방문하지 않은 위치라면
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 1 이상이면 치즈이므로 치즈값을 1 올려줌
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                # 1 보다 작다면 빈 곳이므로 큐에 넣어줌
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny))

while True:
    bfs()
    # 녹은 것을 체크해주기 위한 플래그
    flag = 0

    for i in range(n):
        for j in range(m):
            # 치즈의 값은 원래 1이니 3이면 두변 이상이 붙은 것이므로 녹여줌
            if graph[i][j] >= 3:
                graph[i][j] = 0
                flag = 1
            # 붙은 것이 한변인 것은 치즈 값인 1을 넣어줌
            elif graph[i][j] == 2:
                graph[i][j] = 1

    if flag:
        second += 1
    else:
        break

print(second)
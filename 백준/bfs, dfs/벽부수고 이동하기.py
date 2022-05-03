from collections import deque

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


n, m, k = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dist = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]

def dfs():
    q = deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 1

    while q:
        x, y, broke = q.popleft()

        if x == n-1 and y == m-1:
            return dist[x][y][broke]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not dist[nx][ny][broke]:
                # graph의 값이 0이라 벽을 깨지 않고 갈 수 있는 경우
                if graph[nx][ny] == "0" and dist[nx][ny][broke] == 0:
                    dist[nx][ny][broke] = dist[x][y][broke] + 1
                    q.append((nx, ny, broke))

                # 깰수 있는 벽이 더 있을경우
                elif graph[nx][ny] == "1" and broke < k and dist[nx][ny][broke] == 0:
                    dist[nx][ny][broke + 1] = dist[x][y][broke] + 1
                    q.append((nx, ny, broke + 1))

    return -1

print(dfs())
from collections import deque
import sys

input = sys.stdin.readline  # 빠른 입출력 위한 코드

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R':  # 빨간구슬 위치
            rx, ry = i, j
        elif graph[i][j] == 'B':  # 파란구슬 위치
            bx, by = i, j

# 상 하 좌 우로 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = [(rx, ry, bx, by)]
    count = 0

    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if count > 10:  # 움직인 횟수가 10회 초과면 -1 출력
                print(-1)
                return
            if graph[rx][ry] == 'O':  # 현재 빨간 구슬의 위치가 구멍이라면 count출력
                print(count)
                return

        for i in range(4):
                nrx, nry, nbx, nby = rx, ry, bx, by

                # 벽 또는 구멍을 만날때까지 한방향으로 쭉 탐색
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    # 벽을 만난 경우 벽을 만나기 전칸으로 이동
                    if graph[nrx][nry] == "#":
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] == "O":
                        break
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == "#":
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] == "O":
                        break
                # 파랑구슬이 O에 먼저 도달하거나 동시에 도달하면 안되므로 없는 것으로 침
                if graph[nbx][nby] == "O":
                    continue

                # 둘의 좌표가 같은경우 절대값을 비교하여 더 많이 이동한 구슬이 -dx[i], -dy[i]를 하여 좌표를 한칸 옮겨줌
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))

        count += 1
    # 10번 내에도 못들어가는 경우
    print(-1)

bfs(rx,ry,bx,by)
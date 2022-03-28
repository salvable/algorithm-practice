from collections import deque

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 일자로 쭉 이동
            while True:
                # 범위를 벗어날 시 종료
                if not (0 <= nx < H and 0 <= ny < W):
                    break
                # 벽을 만나도 종료
                if board[nx][ny] == "*":
                    break
                # 이미 방문한 좌표의 설치 거울의 개수가 현재 설치 개수보다 작으면 종료
                if visited[nx][ny] < visited[x][y] + 1:
                    break

                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dx[i]
                ny = ny + dy[i]


W, H = map(int, input().split())
board = [input() for _ in range(H)]

targets = []

for i in range(H):
    for j in range(W):
        if board[i][j] == "C":
            targets.append((i,j))

start_x, start_y = targets[0]
end_x, end_y = targets[1]

visited = [[1e9] * W for _ in range(H)]
bfs(start_x, start_y)

print(visited[end_x][end_y] - 1)

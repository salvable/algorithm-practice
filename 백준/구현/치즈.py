from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
answer = []

dx = [1,-1,0,0]
dy = [0,0,-1,1]


def bfs(visited):
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    # 녹은 치즈 카운트
    count = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                # 치즈 부분은 큐에 넣어주지 않고 count +1
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    count += 1
    return count



while True:
    visited = [[0] * M for _ in range(N)]

    answer.append(bfs(visited))

    if answer[-1] == 0:
        break

print(len(answer) - 1)
print(answer[-2])
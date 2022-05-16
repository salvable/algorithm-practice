from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

answer = 0


def bfs():
    q = deque()
    # x, y 좌표와 뚫은 벽 개수
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, wall = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 범위 안에 있고 방문 하지 않았다면
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][wall] == 0:
                # 벽이 아니라면 이동하고 원래 저장되어있던 값 +1
                if board[nx][ny] == 0:
                    q.append((nx, ny, wall))
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                # 벽을 한번도 부수지 않고 다음 이동할 장소가 벽
                if wall == 0 and board[nx][ny] == 1:
                    q.append((nx, ny, wall + 1))
                    visited[nx][ny][wall + 1] = visited[x][y][wall] + 1
    # 도착하지 못한경우 -1 리턴
    return -1


print(bfs())
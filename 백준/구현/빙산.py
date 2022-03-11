from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 지나간 일수를 기록할 day와 둘 이상으로 나누어지는지 확인할 check
day = 0
check = False

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표상에 있을 경우에
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                # 면이 0이면 현 좌표의 melt_ice 배열을 하나 올려줌
                elif board[nx][ny] == 0:
                    melt_ice[x][y] += 1
    # 연결된 하나의 빙판이므로 1을 리턴
    return 1

while True:
    visited = [[0] * m for _ in range(n)]
    # 녹은 아이스의 개수 저장해 주기 위한 블록
    melt_ice = [[0] * m for _ in range(n)]
    # 빙반 개수
    ice = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] != 0:
                ice += bfs(i,j)

    for i in range(n):
        for j in range(m):
            board[i][j] -= melt_ice[i][j]
            if board[i][j] < 0:
                board[i][j] = 0

    # 빙판이 다 녹아 없어질때까지 분리되지 않는다면
    if ice == 0:
        break

    # 빙판이 두개 이상으로 분리되면
    if ice >= 2:
        check = True
        break

    day += 1

if check:
    print(day)
else:
    print(0)
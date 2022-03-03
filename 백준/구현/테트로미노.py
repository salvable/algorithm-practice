import sys
import json, urllib.request
from collections import deque

input = sys.stdin.readline

# 좌표이동 도구
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 최대값이 될 결과
result = 0


def dfs(x, y, sum, cnt):
    global result

    # 길이가 4인 테트로미노라면 합과 저장된 최댓값중 가장 큰 값을 저장해줌
    if cnt == 4:
        result = max(result, sum)
        return

    # 4 방향으로 움직여 테트로미노를 생성
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != 1:
            visited[nx][ny] = 1
            dfs(nx, ny, sum + board[nx][ny], cnt + 1)
            visited[nx][ny] = 0

def confirm(x,y):
    global result

    for i in range(4):
        # 기준이 되는 점의 좌표를 초기값으로 지정
        tmp = board[x][y]

        for j in range(3):
            index = (i + j) % 4
            nx = x + dx[index]
            ny = y + dy[index]

            if 0 <= nx < n and 0 <= ny < m:
                tmp += board[nx][ny]
            else:
                tmp = 0
                break

        result = max(tmp,result)

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,board[i][j],1)
        visited[i][j] = 0
        # ㅏ,ㅓ,ㅜ,ㅗ, 모양에 대한 확인
        confirm(i,j)

print(result)
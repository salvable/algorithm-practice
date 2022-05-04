from collections import deque

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# 가만히 서있는 경우와 대각 이동까지 총 9 방향
dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]
dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]

graph = deque([list(input().strip()) for _ in range(8)])


def bfs():
    q = deque()
    # 가장 왼쪽 하단 값
    q.append((7, 0))
    move = 0

    while q:
        # 큐의 길이만큼 for문을 돌려 하나의 좌표로부터 이동을 모두 완료한 후 move + 1
        for i in range(len(q)):
            x, y = q.popleft()

            if graph[x][y] == "#":
                continue
            # 도착지점이면 1 리턴
            if x == 0 and y == 7:
                return 1

            for j in range(9):

                nx = x + dx[j]
                ny = y + dy[j]
                if 0 > nx or 8 <= nx or 0 > ny or 8 <= ny:
                    continue
                # 빈칸이면 이동
                if graph[nx][ny] == ".":
                    q.append((nx, ny))

        # 맵의 제일 마지막 행 삭제
        graph.pop()
        # 가장 위에 빈칸으로 이루어진 행 삽입
        graph.appendleft([".", ".", ".", ".", ".", ".", ".", "."])
        move += 1
        # move가 9가 되면 모든 벽이 아래로 밀려서 사라지므로 1을 리턴
        if move == 9:
            return 1

    return 0

print(bfs())

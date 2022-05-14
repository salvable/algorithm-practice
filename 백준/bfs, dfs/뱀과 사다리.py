from collections import deque
import sys
input = sys.stdin.readline

# 사다리 n, 뱀 m
n, m = map(int, input().split())
board = [0] * 101
visited = [False] * 101
ladder = dict()
trap = dict()


def bfs():
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        now = q.popleft()

        # 주사위는 1~6 이므로
        for i in range(1,7):
            next_node = now + i

            # 범위안에 있고 방문하지 않은 경우에
            if 0 < next_node <= 100 and visited[next_node] == False:
                if next_node in ladder.keys():
                    next_node = ladder[next_node]

                if next_node in trap.keys():
                    next_node = trap[next_node]

                if visited[next_node] == False:
                    visited[next_node] = True
                    board[next_node] = board[now] + 1
                    q.append(next_node)

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    trap[x] = y

bfs()

print(board[100])

from collections import deque

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]


def bfs(start_a, start_b, end_a, end_b):
    q = deque()
    q.append((start_a,start_b))

    while q:
        x,y = q.popleft()

        if x == end_a and y == end_b:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx,ny))


tc = int(input())
while tc:
    l = int(input())
    visit = [[0]*l for _ in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(0)
        tc -= 1
        continue
    bfs(x1, y1, x2, y2)
    print(visit[x2][y2])
    tc -= 1

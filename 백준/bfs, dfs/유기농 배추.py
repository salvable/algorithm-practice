from collections import deque
from itertools import combinations
from itertools import product
import heapq
from bisect import bisect_left, bisect_right
import sys
from collections import Counter
INF = int(1e9)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph,a,b):
    visit[a][b] = 1
    q = deque()
    q.append((a,b))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append((nx,ny))

for i in range(t):
    count = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    visit = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1 and visit[a][b] == 0:
                bfs(graph, a, b)
                count += 1

    print(count)

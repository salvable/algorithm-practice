from collections import deque
from itertools import combinations
from itertools import product
import heapq
from bisect import bisect_left, bisect_right
import sys
from collections import Counter
INF = int(1e9)

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
visit = [0] * (N+1)

for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

def bfs(visit, start):
    visit[start] = 1
    q = deque([start])

    while q:
        now = q.popleft()
        print(now, end=" ")

        for i in range(1,N+1):
            # 방문하지 않았고 해당 노드가 연결되어있다면
            if visit[i] == 0 and graph[now][i] == 1:
                visit[i] = 1
                q.append(i)

def dfs(start, visit):
    visit[start] = 1
    print(start, end=" ")

    for i in range(1,N+1):
        if graph[start][i] == 1 and visit[i] == 0:
            dfs(i,visit)


dfs(V,visit)
visit = [0] * (N+1)
print()
bfs(visit,V)

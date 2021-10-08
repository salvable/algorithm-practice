from collections import deque
from itertools import combinations
from itertools import product
import heapq
from bisect import bisect_left, bisect_right
import sys
from collections import Counter
INF = int(1e9)

from sys import stdin
read = stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    visit[start] = 1
    answer = 0

    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visit[i] == 0:
                answer += 1
                visit[i] = 1
                q.append(i)
    print(answer)

bfs(1)

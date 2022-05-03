import copy
import os
from bisect import bisect_left, bisect_right
from collections import Counter
import heapq
from collections import deque
from sys import stdin
import math
from itertools import combinations, permutations, combinations_with_replacement, product
import requests
from collections import deque

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 각각은 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
graph = []
door = []


for i in range(n):
    graph.append(input().strip())
    for j in range(n):
        if graph[i][j] == "#":
            door.append((i, j))

x, y = door[0]
end_x, end_y = door[1]

def bfs():
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0
    q = deque()

    for i in range(4):
        # x,y 좌표와 direction, mirror
        q.append((x,y,i,0))

    while q:
        x, y, direction, m = q.popleft()

        while True:
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                break






print(bfs())
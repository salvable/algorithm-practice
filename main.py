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
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())
result = 0

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x,y):
    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위안에 있고 다음 값이 더 클때에만
            if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx,ny))

    print(dp)

    return dp[x][y] + 1

for i in range(n):
    for j in range(n):
        result = max(result,dfs(i,j))

print(result)
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
from copy import deepcopy
import math

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, k = map(int, input().split())
q = deque()
q.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
    now = q.popleft()
    # 해당 위치가 k 의 위치라면 출력
    if now == k:
        print(visited[now])
        break

    # 순간이동 처리
    if 0 < now*2 < 100001 and visited[now*2] == -1:
        visited[now*2] = visited[now]
        q.appendleft(now*2)
    # 뒤로 한칸 처리
    if 0 <= now-1 < 100001 and visited[now-1] == -1:
        visited[now-1] = visited[now] + 1
        q.append(now-1)
    # 앞으로 한칸 처리
    if 0 <= now+1 < 100001 and visited[now+1] == -1:
        visited[now+1] = visited[now] + 1
        q.append(now+1)

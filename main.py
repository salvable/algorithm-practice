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

gold = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

gold.sort()
bag.sort()

answer = 0
q = []

for b in bag:
    # 보석이 존재하고 bag에 넣을 수 있다면
    while gold and b >= gold[0][0]:
        heapq.heappush(q, -gold[0][1])
        heapq.heappop(gold)

    if q:
        answer += heapq.heappop(q)

    elif not gold:
        break

print(-answer)
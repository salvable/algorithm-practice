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

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

testCase = int(input())

for _ in range(testCase):
    a, b = map(int, input().split())

    visited = [0] * 10000
    q = deque()
    # 현재값과 시행한 문자열을 넣어줌
    q.append((a, ""))

    while q:
        number, path = q.popleft()
        visited[number] = 1

        if number == b:
            print(path)
            break
        # D
        target = (2*number) % 10000
        if not visited[target]:
            q.append((target, path + "D"))
            visited[target] = 1
        # S`
        target = (number-1) % 10000
        if not visited[target]:
            q.append((target, path + "S"))
            visited[target] = 1
        #L
        target = (10 * number + (number // 1000)) % 10000
        if not visited[target]:
            q.append((target, path + "L"))
            visited[target] = 1
        #R
        target = (number // 10 + (number % 10) * 1000) % 10000
        if not visited[target]:
            q.append((target, path + "R"))
            visited[target] = 1

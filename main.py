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

n, r, c = map(int, input().split())
answer = 0

def solve(x, y, n):
    global answer

    # x,y 좌표가 해당 좌표라면
    if x == r and y == c:
        print(answer)
        exit(0)
    if n == 1:
        answer += 1
        return
    # 범위 안에 있지 않을 경우 그 블록 스킵
    if not (x <= r < x+n and y <= c < y+n):
        answer += n * n
        return

    temp = n // 2
    solve(x,y,temp)
    solve(x,y+temp,temp)
    solve(x+temp,y,temp)
    solve(x+temp,y+temp,temp)

solve(0, 0, 2 ** n)
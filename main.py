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

n, m = map(int, input().split())

listen = set()
see = set()

for _ in range(n):
    listen.add(input().strip())

for _ in range(m):
    see.add(input().strip())

result = sorted(list(listen & see))

print(len(result))

for i in result:
    print(i)
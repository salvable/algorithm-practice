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

n = int(input())
dp = [0 for _ in range(31)]
# 2일때 3가지이므로 초기화, 짝수일때만 생성 가능
dp[2] = 3

# n = 4 일때 dp[2] * dp[2] + 2
# n = 6 일때 dp[2] * dp[4] dp
for i in range(4, 31, 2):
    dp[i] = dp[2] * dp[i - 2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2
print(dp[n])
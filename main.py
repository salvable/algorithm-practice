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


n = int(input())
dp = [i for i in range(n + 1)]
dp[1] = 0
arr = [i for i in range(n + 1)]
arr[1] = 0

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    arr[i] = i - 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        arr[i] = i // 3
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        arr[i] = i // 2

print(dp[n])
print(n, end=" ")

temp = n
while arr[temp] != 0:
    print(arr[temp], end=" ")
    temp = arr[temp]
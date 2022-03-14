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

n = int(input())

dp = [0] * 1001

# n이 1일떄 1개 2일때 2개 3일때 3개 4일때 5개 .... dp[i] = dp[i-1] + dp[i-2]
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
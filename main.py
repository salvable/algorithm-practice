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

str1 = ' ' + sys.stdin.readline().rstrip()
str2 = ' ' + sys.stdin.readline().rstrip()

dp = [[0] * (len(str2)) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])

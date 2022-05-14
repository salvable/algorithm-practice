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


n = int(input())
dic = dict()

arr = list(map(int, input().split()))

sort_setArr = sorted(set(arr))

# 정렬된 sort_setArr 과 i 로  몇개보다 작은지 카운팅
for i in range(len(sort_setArr)):
    dic[sort_setArr[i]] = i

for i in arr:
    print(dic[i], end=" ")
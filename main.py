import os
from bisect import bisect_left, bisect_right
from collections import Counter
import heapq
from collections import deque
from sys import stdin
import sys
import math
from itertools import combinations, permutations, combinations_with_replacement, product
import requests

import json, urllib.request

from collections import deque

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

result = 0

# a는 정렬 했으니 0번 인덱스 값이 가장 작으므로 시간복잡도를 위해 0 인덱스를 사용
for i in range(n):
    result += a[0] * max(b)
    a.pop(0)
    b.pop(b.index(max(b)))

print(result)
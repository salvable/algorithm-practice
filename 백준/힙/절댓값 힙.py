import heapq
from bisect import bisect_left, bisect_right
import sys
from collections import Counter
INF = int(1e9)

q = []
n = int(input())

for i in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(q,(abs(x),x))
    elif x == 0:
        if q:
            item = heapq.heappop(q)
            print(item[1])
        else:
            print(0)

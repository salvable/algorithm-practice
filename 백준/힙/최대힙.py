import heapq
import sys
INF = int(1e9)

q = []
n = int(input())

for i in range(n):
    x = int(sys.stdin.readline())

    if x > 0:
        heapq.heappush(q,(-x,x))
    elif x == 0:
        if q:
            item = heapq.heappop(q)
            print(item[1])
        else:
            print(0)

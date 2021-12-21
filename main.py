from itertools import combinations, permutations
from itertools import product
from bisect import bisect_left, bisect_right
from collections import Counter
import heapq
from collections import deque
from sys import stdin
import sys

def find(parent, x):
    if parent[x] != x:
        return find(parent,parent[x])

    return parent[x]

def union(parent,x,y):
    a = find(parent, x)
    b = find(parent, y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int, input().split())
parent = [i for i in range(v+1)]

edge = []
result = 0

for _ in range(e):
    a, b, dist = map(int, input().split())

    edge.append((dist,a,b))

#dist 기준으로 정렬
edge.sort()

for cost, a, b in edge:

    # 같은 루트노드를 가지지 않아 서로 연결할 경우 사이클이 생기지 않을 경우에
    if find(parent,a) != find(parent,b):
        union(parent, a, b)
        result += cost

print(result)
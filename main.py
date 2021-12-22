from itertools import combinations, permutations
from itertools import product
from bisect import bisect_left, bisect_right
from collections import Counter
import heapq
from collections import deque
from sys import stdin
import sys
import math

n = int(input())
parent = [i for i in range(n+1)]

planet = []
edge = []

def find(parent, x):
    if parent[x] != x:
        return find(parent,parent[x])

    return parent[x]


def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(n):
    x, y, z = map(int, input().split())
    planet.append((x, y, z))


# 점들의 사이 거리를 모두 계산하여 간선 배열에 저장한뒤 길이가 짧은 순으로 정렬
for i in range(n-1):
    for j in range(i+1, n):
        dist = min(abs(planet[i][0]-planet[j][0]),abs(planet[i][1]-planet[j][1]),abs(planet[i][2]-planet[j][2]))
        edge.append((dist,i,j))

edge.sort()

result = 0

for e in edge:
    cost, x, y = e

    if find(parent,x) != find(parent,y):
        union(parent,x,y)
        result += cost

print(cost)




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
        return find(parent, parent[x])

    return x

def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
parent = [i for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())

    # 입력받은 두 수가 사이클이 돌면 출력 후 멈춤
    if find(parent,x) == find(parent,y):
        print(i+1)
        break

    union(parent, x, y)

else:
    print(0)

from bisect import bisect_left, bisect_right
from collections import Counter
import heapq
from collections import deque
from sys import stdin
import sys
import math
from itertools import combinations, permutations, combinations_with_replacement, product

n = int(input())
arr = [i+1 for i in range(n)]


cases = list(permutations(arr))

for case in cases:

    for i in case:
        print(i, end=" ")
    print("")

from itertools import combinations, permutations
from itertools import product
from bisect import bisect_left, bisect_right
from collections import Counter
import heapq
from collections import deque
from sys import stdin
import sys
import math

a, b = input().split()

answer = []

# b와 a의 차이만큼 반복문을 돌려 확인
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1
    answer.append(count)

print(min(answer))
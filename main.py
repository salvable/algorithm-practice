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


s = list(input())

word = ""
answer = ""
# <를 만나면 True로 받아 올바르게 출력, False면 statck에 넣어 뒤집어 출력
flag = False

for i in s:
    if not flag:
        if i == "<":
            flag = True
            word += i
        elif i == " ":
            word += i
            answer += word
            word = ""
        else:
            word = i + word

    else:
        word += i
        if i == ">":
            flag = False
            answer += word
            word = ""

answer += word

print(answer)
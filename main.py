import os
from bisect import bisect_left, bisect_right
from collections import Counter
import heapq
from collections import deque
from sys import stdin
import math
from itertools import combinations, permutations, combinations_with_replacement, product
import requests
import sys
import json, urllib.request
from collections import deque

n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소기 위치
board[x][y] = 2
answer = 1

while True:
    check = False

    for i in range(4):
        # 왼쪽으로 회전
        d = (d + 3) % 4
        nx = dx[d] + x
        ny = dy[d] + y

        # 청소하지 않은 자리라면
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            x, y = nx, ny
            answer += 1
            check = True
            break

    # 4방향이 이동 불가함
    if not check:
        # 후진하는 방향도 벽이면
        if board[x-dx[d]][y-dy[d]] == 1:
            break
        else:
            x, y = x - dx[d], y - dy[d]

print(answer)


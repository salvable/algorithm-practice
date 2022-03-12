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
input = sys.stdin.readline

def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]

    # 좌상단, 우상단, 우하단, 좌하단의 방향
    if clockwise:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
    else:
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]

    left_up = (0, 0)
    right_up = (0, n - 1)
    right_down = (n - 1, n - 1)
    left_down = (n - 1, 0)
    # 각 네지점 1로 초기화
    answer[left_up[0]][left_up[1]] = 1
    answer[right_up[0]][right_up[1]] = 1
    answer[right_down[0]][right_down[1]] = 1
    answer[left_down[0]][left_down[1]] = 1

    count = 0

    if n % 2 == 0:
        case = n // 2
    else:
        case = n // 2 + 1

    while case > 0:
        index = (0 + count) % 4
        nx, ny = left_up[0] + dx[index], left_up[1] + dy[index]
        if answer[nx][ny] == 0:
            answer[nx][ny] = answer[left_up[0]][left_up[1]] + 1
            left_up = (nx, ny)

        index = (1 + count) % 4
        nx, ny = right_up[0] + dx[index], right_up[1] + dy[index]
        if answer[nx][ny] == 0:
            answer[nx][ny] = answer[right_up[0]][right_up[1]] + 1
            right_up = (nx, ny)

        index = (2 + count) % 4
        nx, ny = right_down[0] + dx[index], right_down[1] + dy[index]
        if answer[nx][ny] == 0:
            answer[nx][ny] = answer[right_down[0]][right_down[1]] + 1
            right_down = (nx, ny)

        index = (3 + count) % 4
        nx, ny = left_down[0] + dx[index], left_down[1] + dy[index]
        if answer[nx][ny] == 0:
            answer[nx][ny] = answer[left_down[0]][left_down[1]] + 1
            left_down = (nx, ny)

        print(answer)

        index = (0 + count) % 4
        nx, ny = left_up[0] + dx[index], left_up[1] + dy[index]
        while answer[nx][ny] == 0:
            answer[nx][ny] = answer[left_up[0]][left_up[1]] + 1
            left_up = (nx, ny)
            nx, ny = nx + dx[index], ny + dy[index]

        index = (1 + count) % 4
        nx, ny = right_up[0] + dx[index], right_up[1] + dy[index]
        while answer[nx][ny] == 0:
            answer[nx][ny] = answer[right_up[0]][right_up[1]] + 1
            right_up = (nx,ny)
            nx, ny = nx + dx[index], ny + dy[index]

        index = (2 + count) % 4
        nx, ny = right_down[0] + dx[index], right_down[1] + dy[index]
        while answer[nx][ny] == 0:
            answer[nx][ny] = answer[right_down[0]][right_down[1]] + 1
            right_down = (nx,ny)
            nx, ny = nx + dx[index], ny + dy[index]

        index = (3 + count) % 4
        nx, ny = left_down[0] + dx[index], left_down[1] + dy[index]
        while answer[nx][ny] == 0:
            answer[nx][ny] = answer[left_down[0]][left_down[1]] + 1
            left_down = (nx,ny)
            nx, ny = nx + dx[index], ny + dy[index]

        if clockwise:
            count += 1
        else:
            count -= 1

        case -= 1
        print(answer)

    return answer

solution(6,True)


[[1000000000.0, 1, 1, 1000000000.0, 1000000000.0, 1000000000.0]
    , [1000000000.0, 0, 1000000000.0, 1, 1, 1000000000.0],
 [1000000000.0, 1000000000.0, 0, 1000000000.0, 1000000000.0, 1000000000.0],
 [1000000000.0, 1000000000.0, 1000000000.0, 0, 1000000000.0, 1000000000.0],
 [1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0, 0, 1000000000.0],
 [1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0, 0]]

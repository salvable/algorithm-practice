import sys

from sys import stdin
from collections import deque

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = []

def getPaper(x,y,n):
    # x,y 를 받은 값으로 첫번째 색으로 설정
    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            # 다른 색이 하나라도 나온다면
            if color != paper[i][j]:
                getPaper(x, y, n // 3)
                getPaper(x, y + n // 3 , n // 3)
                getPaper(x, y + (n // 3) * 2, n // 3)
                getPaper(x + n // 3, y, n // 3)
                getPaper(x + n // 3, y + n // 3, n // 3)
                getPaper(x + n // 3, y + (n // 3) * 2, n // 3)
                getPaper(x + (n // 3) * 2, y, n // 3)
                getPaper(x + (n // 3) * 2, y + n // 3, n // 3)
                getPaper(x + (n // 3) * 2, y + (n // 3) * 2, n // 3)
                return

    if color == 0:
        result.append(0)
    elif color == -1:
        result.append(-1)
    else:
        result.append(1)


getPaper(0,0,n)

print(result.count(-1))
print(result.count(0))
print(result.count(1))


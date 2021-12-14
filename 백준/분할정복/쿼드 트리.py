import sys

from sys import stdin
from collections import deque

n = int(sys.stdin.readline())
tree = [list(map(int,(input()))) for _ in range(n)]
result = []

def getTree(x,y,n):
    # x,y 를 받은 값으로 첫번째 색으로 설정
    color = tree[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            # 다른 색이 하나라도 나온다면
            if color != tree[i][j]:
                result.append("(")
                getTree(x, y, n // 2)
                getTree(x, y + n // 2, n // 2)
                getTree(x + n // 2, y, n // 2)
                getTree(x + n // 2, y + n // 2, n // 2)
                result.append(")")
                return

    result.append(color)

getTree(0,0,n)

print("".join(map(str,(result))))


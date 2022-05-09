import math

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

import sys
input = sys.stdin.readline

n = int(input())

# 0의 개수
zero = 0

# 배열을 거꾸로 돌며 0 이 아닐떄 break
for i in str(math.factorial(n))[::-1]:
    if i != "0":
        break

    zero += 1

print(zero)
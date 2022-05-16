import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 조합 공식 이용
up = math.factorial(N)
down = (math.factorial(N-M)) * (math.factorial(M))

answer = up//down

print(answer)
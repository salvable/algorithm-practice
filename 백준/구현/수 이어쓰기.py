import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
length = len(str(n))
result = 0

# 자리수에 따라 1-9는 9개  10 - 99 는 90 * 2 = 180 ...

# length -1 까지 자리수를 다 구해준 값이 result 에 저장됨
for i in range(length-1):
    result += 9 * 10 ** i * (i + 1)

print(result + (n - 10 ** (length-1) + 1) * length)
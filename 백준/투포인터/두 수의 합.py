import sys

read = lambda: sys.stdin.readline().rstrip()

n = int(read())
arr = list(map(int, read().split()))
x = int(read())

arr.sort()

# 투포인터 사용
start, end = 0, n-1
answer = 0

while start < end:
    temp = arr[start] + arr[end]

    if temp == x:
        answer += 1

    if temp < x:
        start += 1
    else:
        end -= 1

print(answer)

from collections import deque

import sys

arr = deque()

while True:
    a, b = map(int, input().split())

    # a,b 모두 0이면 중지
    if a == 0 and b == 0:
        break

    arr.append((a,b))

while arr:
    a, b = arr.popleft()

    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n-1
diff = 1e9
answer = [0, 0]

while left < right:
    result = arr[left] + arr[right]

    if abs(result) < diff:
        answer = [left, right]
        diff = abs(result)

    if result > 0:
        right -= 1
    elif result < 0:
        left += 1
    else:
        break

print(arr[answer[0]], arr[answer[1]])
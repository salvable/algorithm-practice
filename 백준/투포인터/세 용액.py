import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

diff = 1e9
answer = []

# i 는 0 부터 n-3까지 돌며 i이후 두 용액을 더하여 값을 비교
for i in range(n-2):
    left = i + 1
    right = n - 1

    while left < right:
        _sum = arr[i] + arr[left] + arr[right]

        if abs(_sum) <= diff:
            diff = abs(_sum)
            answer = [arr[i], arr[left], arr[right]]

        if _sum < 0:
            left += 1
        elif _sum > 0:
            right -= 1
        else:
            break

print(answer[0], answer[1], answer[2])
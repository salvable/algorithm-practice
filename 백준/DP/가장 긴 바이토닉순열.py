import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))


up_arr = [1] * n
down_arr = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            up_arr[i] = max(up_arr[i], up_arr[j] + 1)

# 거꾸로 탐색하여 증가하는 수열 기록
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):

        if arr[i] > arr[j]:
            down_arr[i] = max(down_arr[i], down_arr[j] + 1)

dp = [0] * n

for i in range(n):
    dp[i] = up_arr[i] + down_arr[i] - 1

print(max(dp))

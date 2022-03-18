import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
dp = arr[:]

for i in range(1,n):
    for j in range(i):
        # 지금 수보다 작을경우
        if dp[j] < dp[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))
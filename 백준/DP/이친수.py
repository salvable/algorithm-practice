import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 91

# n이 1일떄 1개 2일떄 1개 3일때 2개 4일때 3개 .... dp[i] = dp[i-1] + dp[i-2]
dp[1] = 1
dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1001

# n이 1일떄 1개 2일때 3개 3일때 5개 4일때 11개 .... dp[i] = dp[i-1] + 2 * dp[i-2]
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n] % 10007)
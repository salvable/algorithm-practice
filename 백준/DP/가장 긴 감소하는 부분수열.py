import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        # 현재 위치 i와 이전에 있는 j 위치와 비교하여 더 작다면 dp[j] + 1 과  dp[i] 중 작은값 선택하여 가져감
        if arr[i] < arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

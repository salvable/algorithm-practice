import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

coin.sort()

dp = [1e9] * (k + 1)
dp[0] = 0

for i in range(n):
    for j in range(coin[i],k+1):
        #dp[j] 값과 dp[j - 해당 코인값]에서 1 더한값
        # 3원짜리로 돌고 있을때 4원을 비교하면 4-3을 하여 dp[1]값과 코인 3원을 사용하여 총 2개를 사용한 값과 기존 최솟값과 비교
        dp[j] = min(dp[j], dp[j-coin[i]] + 1)

if dp[-1] == 1e9:
    print(-1)
else:
    print(dp[k])
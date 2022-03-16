import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int,input().split())
coin = []

for i in range(n):
    c = int(input())
    coin.append(c)

dp = [0] * (k + 1)
dp[0] = 1

# ex) 1,2,5
for i in coin:
    for j in range(i,k+1):
        if j-i >= 0:
            # 해당 값에서 해당 coin만큼 뻇을때 dp에 저장된 값을 더해줌
            # 값어치가 4이고 coin이 2일때 coin 2원을 쓴다고 가정하고 dp[2]에 있는 값을 가져와 씀
            dp[j] += dp[j-i]

print(dp[k])
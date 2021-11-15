n = int(input())
grape = [0]
for i in range(n):
    grape.append(int(input()))

dp = [0]

# 첫번째 포도주를 먹을때 최댓 값과 두번째를 선택할때 최댓값을 dp에 붙여줌
dp.append(grape[1])
dp.append(grape[1] + grape[2])

if n < 2:
    print(dp[1])

else:
    for i in range(3, n + 1):
        # 해당 포도주를 안먹는 경우, 한칸 전에 있는 포도주와 현재 포도주를 먹는경우, 두칸전에 있는 포도주와 현재 포도주를 먹는 값중 최댓값을 선택
        dp.append(max(dp[i-1],dp[i-3] + grape[i-1] + grape[i], dp[i-2] + grape[i]))

print(dp[n])

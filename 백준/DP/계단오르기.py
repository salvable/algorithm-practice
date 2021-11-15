N = int(input())

stair = [0]
for _ in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[1])

else:
    # dp 리스트 생성후 1,2번에 각각 값을 추가
    dp = [0] * (N + 1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    # 3번쨰 발판부터 한칸 전에 있는 발판을 밟을것인지 두칸 전에 있는 발판을 밟을 것인지 선택해야함
    for i in range(3, N+1):

        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2] + stair[i])

    print(dp[N])

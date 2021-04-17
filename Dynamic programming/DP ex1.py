x = int(input())



#dp 테이블 초기화 x는 1~30000
dp = [0]* 30001


for i in range(2,x+1):

    # 1로 뺄 경우
    dp[i] = dp[i-1] + 1

    if i%2:
        dp[i] = min(dp[i],dp[i//2] +1)
    if i%3:
        dp[i] = min(dp[i],dp[i//3] +1)
    if i%5:
        dp[i] = min(dp[i],dp[i//5] +1)

print(dp[x])

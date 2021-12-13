n = int(input())

# 각 자릿수에 따른 갯수를 기록할 리스트
dp = [[0] * 10 for _ in range(n+1)]

# n이 1일때 0을 제외한 모든 숫자는 1로 초기화 해줌
for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        # 0 일경우 계단수가 1 하나로 한정
        if j == 0:
            dp[i][j] = dp[i-1][1]
        # 9 일 결루 계단수가 8로 한정
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        # 나머지는 각 수의 위 아래로 사용 가능
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)

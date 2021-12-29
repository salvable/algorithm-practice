n = int(input())
T = [0 for _ in range(n+1)]
P = [0 for _ in range(n+1)]

for i in range(n):
    a, b = map(int, input().split())
    T[i] = a
    P[i] = b

dp = [0 for _ in range(n+1)]

# 역순으로 진행하여 dp를 쌓아가며 탐색
for i in range(len(T)-2,-1,-1):
    #날짜를 초과하지 않는 경우
    if T[i] + i <= n:
        # 하루 뒤 값이 더 크면 그것을 가져가고 현재값과 현재값 + T[i]일 이후 값을 가져가는게 더 크면 그 값을 저장
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
    else:
        dp[i] = dp[i+1]

print(dp[0])
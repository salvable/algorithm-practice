n = int(input())

line = []

for _ in range(n):
    a, b = map(int, input().split())
    line.append((a,b))

# line의 첫번째 원소로 정렬한뒤 두번째 원소로 증가하는 수열의 수를 구해준다
line.sort(key=lambda x: x[0])

dp = [1] * n

for i in range(n):
    for j in range(i):
        # 현재 line의 두번째 원소가 현재보다 이전 line들의 원소보다 크고 현재 dp 보다 이전것 + 1이 크다면 갱신해줌
        if line[i][1] > line[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

# 전체 숫자에서 증가하는 수열의 개수를 뺸 것을 출력
print(n-max(dp))

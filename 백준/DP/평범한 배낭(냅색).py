# 냅색문제

n, k = map(int, input().split())

# 무게 가치를 담을 리스트
thing = [[0,0]]

# 무게를 k만큼 담을 수 있는 배낭
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

#i는 i번쨰 물건을 선택하였을때 인덱스
for i in range(1, n+1):
    # j는 무게
    for j in range(1, k+1):
        # i번째 thing의 무게와 가치를 가져와서
        w = thing[i][0]
        v = thing[i][1]

        # 배낭이 버틸수 있는 무게보다 작으면 이전 물건에서 최고의 효율을 보이는 값 입력
        if j < w:
            d[i][j] = d[i-1][j]
        # 배낭이 버틸수 있는 무게면 이전 물건에서 최고의 효율을 보이는 값과 비교하여 입력
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])

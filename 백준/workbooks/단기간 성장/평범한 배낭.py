N, K = map(int,input().split())

things = [[0,0]]

# 무게 K까지 담을수 있는 배낭
knapsack = [[0] * (K+1) for _ in range(N+1)]

for i in range(N):
    things.append(list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,K+1):
        w = things[i][0]
        v = things[i][1]

        # j가 물건의 무게보다 작아 넣지 않는 경우
        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        # 현재 물건을 넣지 않는경우와 넣을때 현재 물건의 무게를 뺀 값중 최댓값을 가져와서 현재물건의 value와 더해줌
        else:
            knapsack[i][j] = max(knapsack[i-1][j],knapsack[i-1][j-w]+v)


print(knapsack[N][K])

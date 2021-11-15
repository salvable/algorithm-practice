n = int(input())
color = []
for i in range(n):
    color.append(list(map(int, input().split())))

# 0,1,2는 각각 RGB
# 2차원 배열에서 0번째 인덱스는 놔두고 1번째 인덱스부터 각각  R,G,B를 고름에 따라 최솟값을 더해준 값을 저장
for i in range(1, len(color)):
    # 0을 선택하면 i-1번쨰 리스트에서 1,2를 선택한 값중 작은 값
    color[i][0] = color[i][0] + min(color[i-1][1],color[i-1][2])
    color[i][1] = color[i][1] + min(color[i-1][0],color[i-1][2])
    color[i][2] = color[i][2] + min(color[i-1][0],color[i-1][1])

print(min(color[len(color)-1][0],color[len(color)-1][1],color[len(color)-1][2]))

n = int(input())


# 초기 좌표
x,y = 1,1

#이동계획 입력
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]

move = ["L","R","U","D"]

for plan in plans:
    for i in range(len(move)):
        if move[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx > n or ny > n or nx < 1 or ny < 1:
        continue

    x , y = nx, ny

print(x,y)

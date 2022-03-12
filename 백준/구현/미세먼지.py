import sys
input = sys.stdin.readline

R, C, T = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

air_cleaner = (0,0)

for i in range(R):
    if board[i][0] == -1 and board[i+1][0] == -1:
        # air_cleaner의 좌표 저장
        air_cleaner = (i, i+1)
        break

# T번동안 반복
for _ in range(T):
    # 옮길 먼지를 임시 저장할 테이블
    temp = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            # 해당 지역의 먼지가 먼지량 / 5 만큼의 양이 이동하므로 5이상인 좌표에 대해서만 적용
            if board[i][j] >= 5:
                dust = board[i][j] // 5
                # 확산할 수 있는 장소를 카운팅 하기위한 변수
                count = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    # 다음에 이동할 좌표가 범위안에 있고 공기청소기가 아닌경우에
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        count += 1
                        temp[nx][ny] += dust

                board[i][j] -= (dust * count)

    #저장해 놓은 먼지를 옮겨주기
    for i in range(R):
        for j in range(C):
            board[i][j] += temp[i][j]

    # 위쪽 반시계 방향
    temp = board[air_cleaner[0]][C-1]
    for i in range(C-2, 0, -1):
        board[air_cleaner[0]][i+1] = board[air_cleaner[0]][i]

    temp2 = board[0][C-1]
    for i in range(air_cleaner[0]-1):
        board[i][C-1] = board[i+1][C-1]
    board[air_cleaner[0]-1][C-1] = temp

    temp = board[0][0]
    for i in range(C-1):
        board[0][i] = board[0][i+1]
    board[0][C-2] = temp2

    for i in range(air_cleaner[0]-1, 1, -1):
        board[i][0] = board[i-1][0]
    board[air_cleaner[0]][1] = 0
    board[1][0] = temp



    # lower boud (오 아래 왼 위 순서)
    temp = board[air_cleaner[1]][C-1]
    for i in range(C-2, 0, -1):
        board[air_cleaner[1]][i+1] = board[air_cleaner[1]][i]

    temp2 = board[R-1][C-1]
    for i in range(R-1, air_cleaner[1], -1):
        board[i][C - 1] = board[i-1][C - 1]
    board[air_cleaner[1]+1][C-1] = temp

    temp = board[R-1][0]
    for i in range(C-1):
        board[R-1][i] = board[R-1][i+1]
    board[R-1][C-2] = temp2

    for i in range(air_cleaner[1]+1, R-1):
        board[i][0] = board[i+1][0]
    board[air_cleaner[1]][1] = 0
    board[R-2][0] = temp

result = 0

for i in board:
    result += sum(i)

# 좌표에 청소기의 값이 -1 이므로 + 2 해줌
print(result + 2)
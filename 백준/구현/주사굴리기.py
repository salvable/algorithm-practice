dx = [0,0,-1,1]
dy = [1,-1,0,0]

#가로 세로, 주사위를 놓은 좌표 x,y  명령의 개수 k
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
oper = list(map(int, input().split()))
dice = [0] * 6

# oper의 값은 1,2,3,4순으로 동 서 북 남
# 주사위의 인덱스 값은 위 북 동 서 남 아래 순

for i in range(k):
    direction = oper[i] - 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 범위를 벗어나면 continue
    if not 0 <= nx < n or not 0 <= ny < m:
        continue

    # 주사위가 도는 방향에 따른 dice 갱신
    if direction == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif direction == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif direction == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny

    print(dice[0])

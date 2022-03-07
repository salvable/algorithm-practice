import sys

input = sys.stdin.readline
length = 19

board = [list(map(int, input().split(" "))) for _ in range(length)]

# 우상, 우, 우하, 하 - 3가지 방향만 고려
dx, dy = [-1, 0, 1, 1], [1, 1, 1, 0]


def is_in(x, y):
    if 0 <= x < length and 0 <= y < length:
        return True
    else:
        return False


def is_omok(x, y, player):
    for k in range(len(dx)):
        # 뒷 좌표
        bx = x - dx[k]
        by = y - dy[k]
        # 맵에서 벗어나거나 player의 돌과 다를경우에만 확인 => 돌이 같을경우 오목 이상이 될수 있음
        if not (0 <= x < length and 0 <= y < length) or board[bx][by] != player:
            nx = x + dx[k]
            ny = y + dy[k]
            cnt = 1
            while True:
                if 0 <= x < length and 0 <= y < length and board[nx][ny] == player:
                    cnt += 1
                else:
                    break
                nx += dx[k]
                ny += dy[k]
            if cnt == 5:
                return True
    else:
        return False


def main():
    for i in range(length):
        for j in range(length):
            if board[i][j] != 0:
                # 오목인지 점검하기
                if is_omok(i, j, board[i][j]):
                    return board[i][j], f'{i + 1} {j + 1}'
    else:
        return 0, 0


winner, pos = main()
if winner != 0:
    print(winner)
    print(pos)
else:
    print(winner)
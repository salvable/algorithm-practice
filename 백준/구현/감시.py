import copy
import sys

input = sys.stdin.readline  # 빠른 입출력 위한 코드

n, m = map(int, input().split())

# 0 북 1 동 2 남 3 서
# 각각은 인덱스 번호 cctv의 감지 방향의 수
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

cctv = []
board = []

for i in range(n):
    arr = list(map(int, input().split()))
    board.append(arr)
    for j in range(m):
        # 좌표가 cctv라면 따로 저장
        if arr[j] in [1 ,2,3,4,5]:
            #cctv 종류, [i][j]좌표
            cctv.append([arr[j],i,j])

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def fill(board, d, x, y):
    for i in d:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            # 다음좌표가 벽이거나 board를 벗어나면 중지
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = "#"


def dfs(index, board):
    global answer

    if index == len(cctv):
        count = 0
        for i in range(n):
            count += board[i].count(0)
        answer = min(count, answer)
        return ;

    temp = copy.deepcopy(board)
    cctv_number, x, y = cctv[index]
    for i in mode[cctv_number]:
        fill(temp, i, x, y)
        dfs(index + 1, temp)
        # 해당 인덱스로 감시하고 board를 다시 딥카피하여 모든경우를 탐색
        temp = copy.deepcopy(board)

answer = int(1e9)
dfs(0, board)

print(answer)
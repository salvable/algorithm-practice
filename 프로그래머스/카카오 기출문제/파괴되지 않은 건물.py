def solution(board, skill):
    answer = 0

    # 누적합을 기록할 2차원 리스트, 종료지점을 잡기 위하여 범위를 길이 +1 값으로 설정
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for t, r1, c1, r2, c2, degree in skill:
        if t == 2:
            temp[r1][c1] += degree
            temp[r1][c2 + 1] -= degree
            temp[r2 + 1][c1] -= degree
            temp[r2 + 1][c2 + 1] += degree
        else:
            temp[r1][c1] -= degree
            temp[r1][c2 + 1] += degree
            temp[r2 + 1][c1] += degree
            temp[r2 + 1][c2 + 1] -= degree

    # 행 누적합
    for i in range(len(temp) - 1):
        for j in range(len(temp[0]) - 1):
            temp[i][j + 1] += temp[i][j]
    # 열 누적합
    for i in range(len(temp[0]) - 1):
        for j in range(len(temp) - 1):
            temp[j + 1][i] += temp[j][i]

            # 1 이상인거 체크
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + temp[i][j] >= 1:
                answer += 1

    return answer
def pythonTest():
    n = 5
    board = [["X","S","X","X","T"],["T","X","S","X","X"],["X","X","X","X","X"],["X","T","X","X","X"],["X","X","T","X","X"]]
    # 선생님이 담길 리스트와 장애물을 설치할 수 있는 리스트
    teacher = []
    space = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == "T":
                teacher.append((i, j))
            elif board[i][j] == "X":
                space.append((i, j))

    def watch(x,y,direction):
        if direction == 0:
            while y >= 0:
                if board[x][y] == "S":
                    return True
                elif board[x][y] == "O":
                    return False
                y -= 1
        if direction == 1:
             while y < n:
                if board[x][y] == "S":
                    return True
                elif board[x][y] == "O":
                    return False
                y += 1
        if direction == 2:
             while x >= 0:
                if board[x][y] == "S":
                    return True
                elif board[x][y] == "O":
                    return False
                x -= 1
        if direction == 3:
             while x < n:
                if board[x][y] == "S":
                    return True
                elif board[x][y] == "O":
                    return False
                x += 1

    def process():
        for x,y in teacher:
            # 선생님의 좌표에서 4방향으로 확인
            for i in range(4):
                if watch(x,y,i):
                    return True
        return False

    find = False

    combination = list(combinations(space,3))

    for data in combination:
        # 장애물을 설치
        for x,y in data:
            board[x][y] = "O"

        # 학생이 한명도 감지되지 않는경우
        if not process():
            find = True
            break
        # 학생이 감지 될 경우 설치한 장애물을 다시 빼줌
        for x,y in data:
            board[x][y] = "X"

    if find:
        print("Yes")
    else:
        print("No")

def pythonTest():
    # 8 X 8로 이루어진 체스판 좌측 최상단이 1,1  나이트의 이동할수 있는 지점 탐색
    x, y = 1, 1

    # 이동가능한 모든 경우의 수
    move_type = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

    #이동 가능한 숫자
    count = 0

    for dx,dy in move_type:
        nx = x + dx
        ny = y + dy
        if 1 <= nx <= 8 and 1 <= ny <= 8:
            count += 1

    print(count)

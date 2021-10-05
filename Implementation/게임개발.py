x, y, direction = 1,1,0

def pythonTest():
    # n X n 크기의 맵 생성
    n = 4

    visited = [[0] * n for _ in range(n)]

    print(visited)

    # 북 동 남 서
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    # x,y 좌표와 바라보고 있는 좌표 direction
    global x, y
    # arr은 맵 정보
    arr = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

    def turn_left():
        global direction
        direction -= 1

        if direction < 0:
            direction = 3

    # 시작지점을 방문 처리
    visited[x][y] = 1
    count = 1

    time = 0
    while True:
        turn_left()

        nx = x + dx[direction]
        ny = y + dy[direction]

        if visited[nx][ny] == 0 and arr[nx][ny] == 0:
            visited[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            time = 0
            continue

        else:
            time += 1

            if time == 4:
                nx = x - dx[direction]
                ny = x - dy[direction]

                if arr[nx][ny] == 0:
                    x = nx
                    y = ny
                    time = 0

                else:
                    break

    print(count)

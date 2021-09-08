def pythonTest():
    arr = [[1,0,2],[0,0,0],[3,0,0]]
    n = 3
    # k 는 바이러스 1~k 까지의 종류를 의미
    k = 3
    # 몇 초 후에 x,y 좌표의 값 출력하라
    second, x1, y1 = 2, 3, 2
    result = 0
    data = []

    for i in range(n):
        for j in range(n):
            # 바이러스가 아니라면
            if arr[i][j] != 0:
                # 바이러스 종류 , 시간, x좌표, y좌표를 추가해줌
                data.append((arr[i][j],0,i,j))

    q = deque(data)

    # 좌 상 우 하 인덱스
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    print(data)

    while q:
        virus, s, x, y = q.popleft()

        # 원하는 초가 되었다면 멈춤
        if s == second:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = virus
                    q.append((arr[nx][ny], s+1, x, y))

    print(arr[x1-1][y1-1])

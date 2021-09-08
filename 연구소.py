def pythonTest():
    n = 7
    arr = [[2,0,0,0,1,1,0],[0,0,1,0,1,2,0],[0,1,1,0,1,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,1,1],[0,1,0,0,0,0,0],[0,1,0,0,0,0,0]]
    temp = [[0]*n for i in range(n)]
    result = 0

    # 좌 상 우 하 이동 방향 인덱스
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    # 바이러스를 퍼트리는 함수
    def virus(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 or nx <= n and ny >= 0 or ny <= n:
                # 빈땅이라면 바이러스 퍼트리기
                if temp[nx][ny] == 0:
                    temp[nx][ny] == 2
                    virus(nx, ny)

    def getScore():
        score = 0
        for i in range(n):
            for j in range(n):
                if temp[i][j] == 0:
                    score += 1
        return score


    def dfs(count):
        global result
        if count == 3:
            for i in range(n):
                for j in range(n):
                    # 울타리를 설치한 temp
                    temp[i][j] = arr[i][j]
            for i in range(n):
                for j in range(n):
                    # 돌면서 바이러스 영역이라면
                    if temp[i][j] == 2:
                        virus(i, j)

            result = max(result,getScore())

        for i in range(n):
            for j in range(n):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    # 울타리 개수
                    count += 1
                    dfs(count)
                    # 과정이 끝나면 다시 빼줌
                    arr[i][j] = 0
                    count -= 1

    dfs(0)
    print(result)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 각각은 세로, 가로선의 수 , 가로
N, M, H = map(int, input().split())

# 가로선이 0개이면 안그어도 i는 i번째를 출력하므로 0 출력
if M == 0:
    print(0)

else:
    graph = [[0] * N for _ in range(H)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1

    def confirm():
        for i in range(N):
            start = i
            for j in range(H):
                # 해당 위치에 다리가 있으면 오른쪽으로 이동
                if graph[j][start]:
                    start += 1
                # 0보다 크고 해당 점 왼쪽 위치에 다리가 있으면 왼쪽으로 이동
                elif start > 0 and graph[j][start-1]:
                    start -= 1
            # 시작 위치가 다르다면 false
            if start != i:
                return False
        return True


    def dfs(count, x, y):
        global answer
        if confirm():
            answer = min(answer, count)
            return
        # count 가 3이거나 answer 가 count 보다 작다면 => 3을 초과하면 -1을 출력하기에
        elif count == 3 or answer <= count:
            return

        for i in range(x,H):
            if i == x:
                k = y
            # 행이 변경되면 처음부터 탐색하기위해 0
            else:
                k = 0

            for j in range(k, N -1):
                # 백트래킹으로 사다리를 놓을 수 있는 경우에 놓아줌
                if not graph[i][j] and not graph[i][j+1]:
                    graph[i][j] = True
                    # 연이어 줄을 그을 수 없으므로 j+2해줌
                    dfs(count+1,i,j+2)
                    graph[i][j] = False

    answer = 4
    dfs(0,0,0)

    if answer > 3:
        print(-1)
    else:
        print(answer)

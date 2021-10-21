from collections import deque

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

# 아기상어의 사이즈
shark_size = 2
shark_x, shark_y = 0, 0

for i in range(n):
    for j in range(n):
        # 아기상어의 좌표 위치라면 좌표를 기록하고 그 위치부터 탐색하기 위해 값을 0으로 바꿔줌
        if arr[i][j] == 9:
            shark_x, shark_y = i,j
            arr[shark_x][shark_y] = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 상어까지의 최단거리를 계산
def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((shark_x, shark_y))
    dist[shark_x][shark_y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 방문한 적이 없고 해당 좌표의 값이 상어 크기보다 작거나 같은경우에만
                if dist[nx][ny] == -1 and arr[nx][ny] <= shark_size:
                    # 한칸씩 이동하므로 + 1 한 값을 넣어줌
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    # 거리 정보를 반환
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = 1e9
    for i in range(n):
        for j in range(n):
            # 방문이 가능하고 먹이의 크기가 1보다 크고 상어의 크기보다 작은경우
            if dist[i][j] != -1 and 1 <= arr[i][j] < shark_size:
                # 가장 가까운 먹이 선택
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]

    # 먹을수 있는 경우가 없을 경우
    if min_dist == 1e9:
        return None

    else:
        return x,y,min_dist


# 먹은 먹이 수 와 양
result = 0
ate = 0

while True:
    value = find(bfs())

    if value == None:
        print(result)
        break

    else:
        shark_x , shark_y = value[0], value[1]
        result += value[2]
        # 먹은 위치의 값은 0으로 초기화
        arr[shark_x][shark_y] = 0
        ate += 1

        # 자기 크기만큼 먹은경우 크기를 늘려주고 먹은 값 초기화
        if ate >= shark_size:
            shark_size += 1
            ate = 0

from collections import deque
import sys

# 맵과 백조를 기록할 리스트
maps = []
bird = []

r, c = map(int, sys.stdin.readline().split())

for i in range(r):
    arr = list(sys.stdin.readline().replace("\n",""))
    maps.append(arr)
    for j in range(len(arr)):
        if arr[j] == "L":
            bird.append((i,j))

# 얼음이 녹는 시간을 기록할 배열
time = [[0 for _ in range(c)] for _ in range(r)]


def melt_ice(map):
    # 방문을 확인하기 위한 리스트와 방향이동을 위한 리스트
    visited = [[0 for _ in range(c)] for _ in range(r)]
    direction = [(0,1),(0,-1),(1,0),(-1,0)]

    queue = deque()

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "." or maps[i][j] == "L":
                #map을 돌며 이동할수 있는 지점과 백조가 있는 지점은 time리스트를 0으로 초기화, 큐에 넣고 방문처리
                queue.append((i, j))
                time[i][j] == 0
                visited[i][j] = True

    # 빙하가 녹는 시간
    melt_time = 0

    while queue:
        x,y = queue.popleft()

        for dx,dy in direction:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and visited[nx][ny] == False:
                queue.append((nx,ny))
                time[nx][ny] = time[x][y] + 1
                visited[nx][ny] = True
                melt_time = time[nx][ny]

    return melt_time


def bfs(start, target, map, mid):
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    queue = deque()
    queue.append(start)
    visited = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]

    while queue:
        x,y = queue.popleft()
        visited[x][y] = True

        for dx,dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and visited[nx][ny] == False:
                visited[nx][ny] = True

                #nx, ny 값이 target의 값이라면 도달 가능하므로 True 리턴
                if nx == target[0] and ny == target[1]:
                    return True

                # 얼음이 녹는데 걸리는 시간이 mid보다 작거나 같으면 이동이 가능하므로 큐에 넣어줌
                if time[nx][ny] <= mid:
                    queue.append((nx,ny))

    return False;

# 이진 탐색을 하기 위한 min, max값 획득
min_value, max_value = 0, melt_ice(maps)

answer = max_value

while min_value <= max_value:
    mid = (max_value + min_value) // 2
    # 출발점, 도착점, 맵, mid값
    if bfs(bird[0],bird[1],maps, mid):
        # True를 리턴받으면 도착 가능하므로 max값을 줄이고 재탐색
        answer = mid
        max_value = mid -1
    else:
        # 도착이 불가능하면 mid값을 올려 얼음을 더 녹게 한 뒤 재탐색
        min_value = mid + 1

print(answer)

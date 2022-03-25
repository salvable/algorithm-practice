import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 맵 좌표
arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    # 시작점을 1로
    arr[x][y] = 1
    direction = [d]

    # g 세대 만큼 반복하여 만들어줌
    for _ in range(g):
        temp = []
        for i in range(len(direction)):
            # 거꾸로 뒤집어 +1 된 값을 더해줌
            temp.append((direction[-i -1] + 1) % 4)
        direction.extend(temp)

    for i in direction:
        nx = x + dx[i]
        ny = y + dy[i]
        arr[nx][ny] = 1
        x, y = nx, ny

result = 0
# 네점이 모두 1인지 확인하여 모두 1이면 result += 1
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            result += 1

print(result)

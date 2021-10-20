# n * n 맵, k개의 사과
n = int(input())
k = int(input())

data = [[0] * (n+1) for i in range(n+1)]

# 사과가 있는 지점은 1로 표시
for _ in range(k):
    x, y = map(int, input().split())
    data[x][y] = 1

# 회전 방향 리스트
l = int(input())
move = []
for _ in range(l):
    x, c = input().split()
    # x 초 뒤 c 방향으로 회전
    move.append((int(x), c))

#direction 이 최초 우측방향이므로 동 남 서 북 순
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 회전
def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction

def simulate():
    # snake 의 x,y좌표
    sx, sy = 1, 1
    # 사과가 1 , 뱀이 2
    data[sx][sy] = 2
    direction = 0

    # 지난 시간과 move리스트에 각각 접근하기 위한 인덱스
    time = 0
    turn_index = 0

    q = [(sx,sy)]

    while True:
        nx = sx + dx[direction]
        ny = sy + dy[direction]

        # 이동하는 곳이 뱀이 아니고 맵 안이라면
        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            # 아무것도 없을 때
            if data[nx][ny] == 0:
                # 옮길자리는 2 로 있었던 자리는 q 에서 뺀뒤 0으로 바꿔줌
                data[nx][ny] = 2
                q.append((nx,ny))
                qx, qy = q.pop(0)
                data[qx][qy] = 0

            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
        # 벽이나 맵 몸통에 부딪힐 경우
        else:
            time += 1
            break

        sx, sy = nx, ny
        time += 1
        # turn index가 move 리스트의 시간과 같다면 회전할 차례이므로
        if turn_index < l and time == move[turn_index][0]:
            direction = turn(direction,move[turn_index][1])
            turn_index += 1

    return time

print(simulate())

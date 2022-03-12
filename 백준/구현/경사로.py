import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]

# 경사로 설치후 지날수 있는 길의 수
result = 0

def confirm(route):
    # 경사로에 세운것을 확인하기 위한 리스트
    arr = [0] * N

    for i in range(N-1):
        # 경사로 높이 차이가 있는경우
        if route[i] != route[i+1]:
            # 차이가 1보다 크면 지날수 없는 길
            if abs(route[i] - route[i+1]) > 1:
                return False
            else:
                # 높은칸에서 낮은칸으로 가는 경우
                if route[i] - route[i+1] == 1:
                    # i+1인덱스에서 L만큼 더하였을 경우 초과하면 경사로 설치 불가
                    if i+1+L > N:
                        return False

                    high = route[i+1]
                    for j in range(i+1, i+1+L):
                        # 해당지점에 경사로가 설치되어 있거나 높이가 다른경우 경사로 설치 불가
                        if arr[j] == 1 or route[j] != high:
                            return False
                        # 아닐경우 경사로 설치
                        arr[j] = 1
                # 낮은 칸에서 높은 칸으로 갈경우
                elif route[i] - route[i+1] == -1:
                    print(i,L)
                    print(route)
                    if i - L < -1:
                        return False

                    high = route[i]
                    for j in range(i, i-L, -1):
                        if arr[j] == 1 or route[j] != high:
                            return False
                        arr[j] = 1
    return True

for i in board:
    if confirm(i):
        result += 1

for i in range(N):
    if confirm([board[j][i] for j in range(N)]):
        result += 1

print(result)
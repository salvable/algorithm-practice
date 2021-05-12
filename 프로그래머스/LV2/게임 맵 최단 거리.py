from collections import deque

def search(start,maps):
    # 상하좌우를 옮기기 위한 값
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    queue = deque()
    queue.append(start)
    
    while queue:
        y,x,value = queue.popleft()
        for i in range(4):
            ny,nx = y + dy[i] , x + dx[i]
            
            # 좌표가 지문은 1,1부터 시작하므로 길이에는 -1, value값에는 +1 
            if ny == len(maps)-1 and nx == len(maps[0])-1:
                return value + 1
            # 범위를 벗어나지 않고 값이 1일 경우
            elif ny >= 0 and ny < len(maps) and nx >= 0 and nx < len(maps[0]) and maps[ny][nx] == 1:
                    # 이미 확인한 값은 0으로 바꿔줌
                    maps[ny][nx] = 0
                    queue.append((ny,nx,value+1))
    #다 돌고 return이 안된경우 -1     
    return -1 
def solution(maps):
    # 0,0 좌표와 그 좌표는 1값을 가지고 시작
    return search((0,0,1), maps)

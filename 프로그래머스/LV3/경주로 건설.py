from collections import deque

def solution(board):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    # 가격을 저장할 2차원 리스트
    arr = [[0] * len(board) for _ in range(len(board))]
    
    q = deque()
    # x,y 좌표와 방향인덱스, 누적가격을 큐에 넣어줌
    q.append((0,0,0,0))
    
    while q:
        x,y,direction, cost = q.popleft()
        
        for next_direction in range(4):
            nx = x + dx[next_direction]
            ny = y + dy[next_direction]
            
            # 맵 안인 경우
            if 0 <= nx < len(board) and 0 <= ny < len(board):
                # 벽이 아닌 경우
                if board[nx][ny] != 1:
                    if x == 0 and y == 0:
                        newCost = cost + 100
                    else:
                        # 방향이 같으면 100원 아니면 600원을 추가
                        if direction == next_direction:
                            newCost = cost + 100
                        else:
                            newCost = cost + 600
                    
                    # 첫 방문이라면 가격을 그냥 넣어줌
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = newCost
                        q.append((nx,ny,next_direction,newCost))
                    # 아닌경우 기존값보다 작은경우최솟값을 넣어줌
                    else:
                        if newCost <= arr[nx][ny]:
                            arr[nx][ny] = newCost
                            q.append((nx,ny,next_direction,newCost))
                    
    return arr[-1][-1]

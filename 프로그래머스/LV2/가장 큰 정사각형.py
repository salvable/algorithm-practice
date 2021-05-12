def solution(board):
    x = len(board[0])
    y = len(board)

    
    #x축과 y축 모두 1이상인 값부터 탐색하는 DP로 풀 예정
    for i in range(1,y):
        for j in range(1,x):
            if board[i][j] == 1:
                # 1,1 부터 위, 왼쪽, 왼쪽위를 비교해서 가장 작은값에 1을 더해주면서 쌓아감
                board[i][j]  = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) + 1
    
    answer = 0
    
    for i in board:
        if(max(i) > answer):
            answer = max(i)
    
    return answer * answer 

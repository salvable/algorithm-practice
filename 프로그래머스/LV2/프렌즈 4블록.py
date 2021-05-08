#편의를 위해 배열을 회전 시킴
def transeBoard(m,n,board):
    temp = [[0] * m for i in range(n)]
    
    for i in range(m):
        for j in range(n):
            temp[j][i] = board[i][j]
    return temp

def find(m,n,board):
    # 2*2가 같은 값인것을 찾음
    findset = set()
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != "0":
                findset.update([(i,j),(i+1,j),(i,j+1),(i+1,j+1)])
    return findset

def bomb(m,n,board,findset):
    # 해당 인덱스의 값을 0으로 바꾸고 지운 후 제일 뒤에 추가 
    for x,y in findset:
        board[x][y] = "0"
    
    for i in range(n):
        tmp = ["0"] * board[i].count("0")
        board[i] = tmp + [z for z in board[i] if z != "0" ]

def solution(m, n, board):
    
    answer = 0
    
    board = transeBoard(m,n,board)
    
    while True:
        findset = find(m,n,board)
        if(len(findset) == 0):
            break
        answer += len(findset)
        bomb(m,n,board,findset)
    
    return answer

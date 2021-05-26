# 자물쇠와 열쇠

# 오른쪽으로 90도 회전 소스코드
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def check(seach_lock):
    # 3으로 나눈 이유는 3배로 늘렸기 때문에 나누어서 가운데 자물쇠에 접근하기 위함
    length = len(seach_lock) // 3
    for i in range(length,length*2):
        for j in range(length,length*2):
            # 값이 1이 아니라면 키가 틀리므로 False리턴 , 다돌았다면 True 리턴
            if seach_lock[i][j] != 1:
                return False
    return True    

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    #탐색을 위해 배열의 길이를 Lock의 3배로 늘림
    seach_lock = [[0] * (n*3) for _ in range(n*3)]
    
    #lock을 늘린 배열의 중앙에 박는 과정
    for i in range(n):
        for j in range(n):
            seach_lock[i+n][j+n] = lock[i][j]
    
    #회전해가면서 (0,0) 부터 (2n-1,2n-1) 까지 확인하면서 lock이 모두 1인지 확인하기

    #90도씩 4번 회전
    for count in range(4):
        key = rotate_90(key)
        
        # 다음 좌표에 대하여 
        for x in range(2*n):
            for y in range(2*n):
                # 열쇠를 넣어봄
                for i in range(m):
                    for j in range(m):
                        seach_lock[x+i][y+j] += key[i][j]
                        
                if check(seach_lock) == True:
                    return True
                
                for i in range(m):
                    for j in range(m):
                        seach_lock[x+i][y+j] -= key[i][j]
                
    return False

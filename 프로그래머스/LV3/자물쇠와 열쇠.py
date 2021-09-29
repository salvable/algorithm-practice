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
    
    # 자물쇠의 크기의 3배로 늘림
    search_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    for i in range(n):
        for j in range(n):   
            search_lock[n+i][n+j] = lock[i][j]
            
    
    for count in range(4):
        key = rotate_90(key)
        
        for x in range(n*2):
            for y in range(n*2):
                # 좌물쇠에 키를 넣는 과정
                for i in range(m):
                    for j in range(m):
                        search_lock[x+i][y+j] += key[i][j]
                if check(search_lock) == True:
                    return True
                
                # 키를 넣은 좌물쇠에서 키를 뺴는 과정
                for i in range(m):
                    for j in range(m):
                        search_lock[x+i][y+j] -= key[i][j]
    
    return False

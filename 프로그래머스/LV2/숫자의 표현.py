def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        # 합을 기록하기 위한 변수
        s = 0
        
        for j in range(i,n+1):
            s += j
            
            # 값을 넘는 순간 break
            if s > n :
                break
            if s == n:
                answer += 1
                break
            
    return answer



# 수학 공식을 이용하면 for문 한번으로도 끝낼수 있다고 한다.

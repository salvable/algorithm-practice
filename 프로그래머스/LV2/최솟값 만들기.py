def solution(A,B):
    answer = 0

    # 제일 작은 값과 큰값을 뽑는 방식으로 접근

    A.sort()
    B.sort()
    
    for i in range(1,len(A)+1):
        answer += A[i-1] * B[-i]
        
        
    return answer

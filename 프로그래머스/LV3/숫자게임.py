def solution(A, B):
    
    if min(A) >= max(B):
        return 0
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    answer = 0
    
    while True:
        
        if A[0] >= B[0]:
            A.pop(0)
        else:
            A.pop(0)
            B.pop(0)
            answer += 1
            
        if len(A) == 0 or len(B) == 0:
            break
    
    return answer

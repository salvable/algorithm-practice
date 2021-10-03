def solution(n):
    answer = 0
    
    # 2로 나눈 값이 나누어 떨어질 경우 TP, 아닐경우 JUMP를 하는 부분으로 접근
    
    while True:
        if n % 2 != 0:
            n -= 1
            answer += 1
        else:
            n = n // 2 
        
        if n == 0:
            break

    return answer

def solution(n,a,b):
    
    answer = 0 

    # 토너먼트에 올라가면 절반으로 들어가는 것을 이용
    while a != b:
        if a % 2 == 1:
            a = a // 2 + 1
        else: 
            a = a // 2

        if b % 2 == 1:
            b = b // 2 + 1
        else:
            b = b // 2
            
        answer += 1
    return answer

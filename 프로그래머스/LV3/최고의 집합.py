def solution(n, s):
    
    # 자연수의 갯수 n이 만들고자하는 s보다 크면 만들지 못하므로 [-1]을 리턴
    if n > s:
        return [-1]
        
    # 두 수간의 곱이 가장 크려면 두 수의 차이가 작아야 하므로 n 으로 나눠준뒤 나머지 값을 돌아가면서 +1 씩 해준다
    answer = []
    remain = s % n
    
    for _ in range(n):
        answer.append(s//n)
    
    while remain != 0:
        for i in range(n):
            if remain == 0:
                break
                
            answer[i] += 1
            remain -= 1
    
    return sorted(answer)

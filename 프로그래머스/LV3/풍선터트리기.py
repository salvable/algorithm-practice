def solution(a):
    # 기본적으로 양쪽 끝은 큰수를 한번 택할 조건이 있으므로 마지막으로 고르면 생존 할 수 있음 
    answer = 2
     
    if 0 <= len(a) <= 2:
        return len(a)
    
    # 각각 양쪽 끝을 값으로 설정
    left = a[0] 
    right = a[-1]
    
    for i in range(1,len(a)-1):
        # 인덱스를 하나씩 돌다가 각각 값보다 작은 수를 만나면 answer + 1 해주고 값을 해당 인덱스 값으로 변경
        if left > a[i]:
            answer += 1
            left = a[i]

        if right > a[-1-i]:
            answer += 1
            right = a[-1-i]
    
    # 중복된다면 중복되는 값을 하나 빼줌
    if right == left:
        return answer - 1
    
    return answer

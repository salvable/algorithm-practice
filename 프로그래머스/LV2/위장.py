def solution(clothes):
    
    dic = dict()
    
    for i,j in clothes:
        # i는 의상의 이름 j는 의상의 종류
        
        if j in dic.keys():
            dic[j] += 1
        else:
            dic[j] = 1
    
    answer = 1
    
    for i in dic.values(): 
        #해당 종류를 입지 않았을 경우까지 포함하여 계산
        answer *= i+1
    
    # 무조건 한개의 의상은 입으므로 아무것도 입지않은 경우의수 뺴줌
    return answer-1

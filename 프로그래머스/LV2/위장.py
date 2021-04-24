def solution(clothes):
    
    dictionary = dict()
    
    for i,j in clothes:
        print(i,j)
        if j not in dictionary:
            dictionary[j] = 1
        else:
            dictionary[j] += 1
    
    answer = 1
    
    for i in dictionary.values():
        # 착용하지 않은경우를 카운트 하기위해 i+1 
        answer *= (i+1)
        
        # 하루 최소 한개는 입으므로 다 안입을 경우를 빼줌
    return answer -1

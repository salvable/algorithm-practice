def solution(msg):
    dic = dict()

    answer = []
    
    #dict 초기화 작업
    for i,char in enumerate(range(ord("A"), ord("Z")+1)):
        dic[chr(char)] = i + 1
    
    start = 0
    idx = 0
    end = 26
    answer = []
    
    while True:
        idx += 1
        # dic에 없을경우
        if msg[start:start+idx] not in dic:
            end += 1
            dic[msg[start:start+idx]] = end
            #현재보다 한번 전에 시행됬던 것을 리스트에 넣어줌(출력할 값)
            answer.append(dic[msg[start:start+idx -1]])
            start = start + idx -1
            idx = 0 
        else:
            # 아닐 경우 마지막에 검색했던 값 출력
            if start + idx - 1 >= len(msg):
                answer.append(dic[msg[start:start+idx-1]])
                break
    
    return answer 

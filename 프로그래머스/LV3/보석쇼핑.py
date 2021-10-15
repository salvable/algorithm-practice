def solution(gems):
    answer = []
    length = len(gems)+1
    set_count = len(set(gems))
    
    #투포인터 인덱스
    start, end = 0, 0

    # 보석의 종류
    dic = dict()
    

    while end < len(gems):
        # 해당 보석이 dic에 없으면 
        if gems[end] not in dic:
            dic[gems[end]] = 1
        else:
            dic[gems[end]] += 1
            
        end += 1
        
        # 적어도 종류별로 하나 이상 포함 했을 경우
        if len(dic) == set_count:
            while start < end:
                # 2개 이상인경우 start 인덱스를 하나 당겨옴
                if dic[gems[start]] > 1:
                    dic[gems[start]] -= 1
                    start += 1
                # 기록한 길이보다 작은경우가 나오면
                elif length > end - start:
                    length = end - start
                    answer = [start+1,end]
                    break
                else:
                    break
                    
    return answer

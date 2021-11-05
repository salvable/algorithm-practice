from itertools import permutations

def solution(k, dungeons):
    #모든 경우의 수를 구해줌
    permutation = list(permutations(dungeons,len(dungeons)))
    
    # 각 케이스별로 탐험 던전횟수를 기록할 리스트
    answer = 0
    # k값을 저장하기 위한 변수
    temp = k
    
    
    for lists in permutation:
        result = 0
        for min_value, consume_value in lists:
            # 현재 피로도가 최소 요구량 보다 작은경우
            if k < min_value:
                break
            
            k -= consume_value
            result += 1
        answer = max(answer,result)
        k = temp
    return answer

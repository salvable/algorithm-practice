def solution(routes):
    answer = 0 
    index = -30001
    
    routes.sort(key = lambda x: x[1])
    
    for i in routes:
        # 현 카메라의 인덱스가 출입 지점보다 작으면 차량을 적발하지 못하므로 카메라를 추가설치함. 추가 설치 하고 index를 바꿔줌
        if index < i[0]:
            answer += 1
            index = i[1]
            
    return answer

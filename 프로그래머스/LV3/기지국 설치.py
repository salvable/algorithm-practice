import math

def solution(n, stations, w):
    answer = 0

    distance = []
    
    # 설치된 기지국 사이에 전파가 닿지 않는 거리를 구해줌
    for i in range(1,len(stations)):
        distance.append((stations[i]-w-1) - (stations[i-1]+w))

    # 시작지점과 끝지점으로 부터 제일 가까운 기지국으로 부터 전파가 닿지 않는 거리를 구해줌
    
    distance.append(stations[0]-w-1)
    distance.append(n - (stations[-1]+w))
    
    for i in distance:
        # 전파가 모두 흐르고 있을경우 넘어감
        if i <= 0: 
            continue
        
        # 최소로 설치하는 방법은 전파가 닿지않는 거리 / ()
        answer += math.ceil(i / ((w*2) + 1))

    return answer

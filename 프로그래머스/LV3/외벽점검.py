from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    
    # 길이를 두배로 늘린 취약점 리스트
    for i in range(length):
        weak.append(weak[i] + n)
    
    # 최솟값을 찾기 위한 값 설정
    answer = len(dist) + 1
    
    # 출발할 좌표
    for s in range(length):
        worker_permutation = list(permutations(dist,len(dist)))
        
        for workers in worker_permutation:
            # 현재 탐색중인 작업자 1로 초기화
            count = 1
            
            # 해당 인원의 탐색이 끝나는 지점
            end = weak[s] + workers[count - 1]
            
            for i in range(s, s + length):
                # 점검 할 수 있는 위치를 벗어나면 
                if end < weak[i]:
                    count += 1
                    # 더 투입이 불가능하면 중지
                    if count > len(dist):
                        break
                    end = weak[i] + workers[count -1]
            
            answer = min(answer,count)
    if answer > len(dist):
        return -1
            
    return answer

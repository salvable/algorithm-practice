from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque([0] * bridge_length)
    current_weight = 0

    while q:
        
        # 1초가 증가하고 차한대가 빠짐
        answer += 1
        w = q.popleft()
        current_weight -= w
        
        if truck_weights:
            # q의 값과 다음에 들어올 차량의 무게가 버틸수 있는지 확인
            if current_weight + truck_weights[0] <= weight:
                current_weight += truck_weights[0]
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    
    
    return answer

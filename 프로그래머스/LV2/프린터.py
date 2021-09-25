from collections import deque

def solution(priorities, location):
    answer = 0
    
    deq = deque([(prioritie,index) for index,prioritie in enumerate(priorities)])
    
    while deq:
        if len(deq) == 1:
            answer += 1
            break
        item = deq.popleft()
        # deq 안 item들의 prioritie의 max값보다 꺼낸 값의 우선도가 낮은경우 
        if item[0] < max(deq)[0] and deq:
            deq.append(item)
        
        else:
            answer += 1
            if item[1] == location:
                break
            
    return answer

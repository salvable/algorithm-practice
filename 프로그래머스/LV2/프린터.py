from collections import deque

def solution(priorities, location):
    answer = 0
    
    deq = deque([(value,i) for i,value in enumerate(priorities)])
    
    
    
    while deq:
        # deque의 길이가 1일때 예외처리
        if len(deq) == 1:
            answer += 1
            break
        # 처음 값을 빼고    
        item = deq.popleft()
        
        #그거를 맥스값과 비교해서 작으면 다시 deque에 넣어줌
        if item[0] < max(deq)[0] and deq:
            deq.append(item)
         #아닐경우 answer 값을 하나 올려줌 
        else:
            answer += 1
            if item[1] == location:
                break
           
    return answer

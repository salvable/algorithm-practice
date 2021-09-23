def solution(progresses, speeds):
    answer = []
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        count = 0    
            
        while progresses and progresses[0] >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        
        if count > 0:
            answer.append(count)
    
    return answer

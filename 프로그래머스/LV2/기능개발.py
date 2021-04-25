def solution(progresses, speeds):
    answer = []
    
    while(progresses):
        # 각각의 진행률마다 스피드만큼 올려줌
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0

        # progresses가 존재하고 제일 첫번째 리스트가 100이상이면 count를 늘리고 pop
        while progresses and progresses[0] >= 100:
            speeds.pop(0)
            progresses.pop(0)
            count += 1

        # 작업이 완료된 개수가 1개 이상이면 리스트에 붙임
        if(count >= 1):
            answer.append(count)
    return answer

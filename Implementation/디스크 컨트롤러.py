import heapq

def solution(jobs):
    answer = 0
    # 시작하기 이전시간, 현재시간, 작업된 수
    start, now, complete = -1,0,0
    q = []
    
    while complete < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                #실행시간을 기준으로 정렬하기 위해 다음과같이 큐에 넣어줌 
                heapq.heappush(q,(job[1],job[0]))
                
        if len(q) > 0:
            # x 는 처리되는 시간 y는 도착시간 
            x,y = heapq.heappop(q)
            start = now
            now += x
            answer += now - y
            complete += 1 
        else:
            now += 1

    return answer // len(jobs)
    

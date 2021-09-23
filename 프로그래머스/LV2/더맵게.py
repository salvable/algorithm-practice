import heapq

def solution(scoville, K):
    q = []
    count = 0 
    
    for s in scoville:
        heapq.heappush(q,s)
        
    while len(q) >= 2:
        first = heapq.heappop(q)

        # 첫번째 원소가 지정한 지수보다 높으면 다시 heapq에 넣고 반복문 탈출
        if first >= K:
            heapq.heappush(q,first)
            break
            
        second = heapq.heappop(q)
        
        newScoville = first + second * 2
        heapq.heappush(q,newScoville)
        count += 1

    # 꺼낸 제일 작은 원소가 k보다 작으면 -1, 아니면 count 리턴
    result = heapq.heappop(q)
    
    if result < K:
        return -1
    
    return count

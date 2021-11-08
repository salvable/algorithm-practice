import heapq

def solution(n, works):
    answer = 0
    heap = []
    
    # work의 합이 n시간보다 작으면 야근을 하지 않으므로 0 리턴
    if sum(works) <=  n:
        return answer 
    
    # 제곱으로 야근지수를 정하므로 큰수부터 1씩 줄이는 방식으로 접근하기 위해 heapq사용
    for i in works:
        heapq.heappush(heap,(-i,i))
    
    while True:
        if n == 0:
            break
            
        # 가장 큰 작업량을 꺼낸뒤 -1한 값을 다시 넣어줌
        work = heapq.heappop(heap)[1] - 1
        heapq.heappush(heap,(-work,work))
        n -= 1
        
    for i in heap: 
        # 제곱한 값을 더해줌
        answer += i[1] ** 2

    return answer

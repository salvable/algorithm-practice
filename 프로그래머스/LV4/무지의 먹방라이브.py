import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    q = []
    
    # 번호와 시간을 함께 저장, heapq를 사용하여 음식을 먹는데 가장 적게 드는 항목이 0에 위치 
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
        
    # 각각의 항목은 먹는데 사용한 시간, 이전에 먹은 음식 시간, 음식 개수를 의미
    eat_time = 0
    pre_time = 0
    foods = len(food_times)
        
    while eat_time + (q[0][0] - pre_time) * foods <= k:
        eat, index = heapq.heappop(q)
        eat_time += (eat - pre_time) * foods
        foods -= 1
        pre_time = eat
    
    # 음식번호를 기준으로 오름차순 정리
    result = sorted(q, key= lambda x: x[1])
    
    # k시간에서 먹은 시간을 빼준것에 남은 음식의 나머지 값의 인덱스를 answer로 설정
    answer = result[(k - eat_time) % foods][1]
        
    return answer

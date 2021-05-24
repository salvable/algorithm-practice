# 해당 문제는 완전탐색으로 진행할 경우 효율성 테스트에서 점수가 나오지 않음.

import heapq

def solution(food_times, k):
    
    # 전체 음식이 k보다 작다면 -1
    if sum(food_times) <= k :
        return -1
    
    heap = []
    
    for i in range(len(food_times)):
        #result 값으로 번호를 받아야 하기 때문에 튜플 형식으로 추가해줌
        heapq.heappush(heap,(food_times[i],i+1))

    #먹는데 소요한 시간 , 이전에 먹은 음식 시간, 남은 음식 개수
    eat_time = 0
    pre_time = 0
    foods = len(food_times)
    
    while eat_time + ((heap[0][0] - pre_time) * foods) <= k:
        popData = heapq.heappop(heap)[0]
        eat_time += (popData - pre_time) * foods
        foods -= 1 
        pre_time = popData
        
    #음식 번호를 기준으로 sort
    result = sorted(heap, key = lambda x : x[1])    
    
    #k에서 먹은시간을 뺀 값에 남은 음식의 나머지 값을 구함
    answer = result[(k-eat_time) % foods][1]
    return answer

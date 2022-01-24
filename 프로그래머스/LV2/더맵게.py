import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while True:

        first = heapq.heappop(scoville)

        if first >= K:
            break

        # 더이상 진행할 원소가 없는 경우
        if len(scoville) == 0:
            return -1

        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        count += 1

    return count
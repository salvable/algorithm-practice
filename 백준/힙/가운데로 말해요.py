import heapq
import sys

input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []
for i in range(n):
    num = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    # 둘다 길이가 1 이상이고 큰쪽의 heap의 첫번째 원소가 작은쪽의 첫번째 원소보다 작을경우 바꿔줌
    if len(left_heap) >= 1 and len(right_heap) >= 1 and left_heap[0] * -1 > right_heap[0]:
        left_value = heapq.heappop(left_heap[0]) * -1
        right_value = heapq.heappop(right_heap[0])

        heapq.heappush(left_heap, right_value * -1)
        heapq.heappush(right_heap, left_value)

    # 작은쪽 heap의 첫번째 원소에 -1을 곱한 값을 출력
    print(left_heap[0] * -1)

import heapq
import sys

input = sys.stdin.readline

N = int(input())

left_heap = []
right_heap = []

for i in range(N):
    num = int(input())

    # 각각 최대힙, 최소힙으로 만들어줌 left의 첫번쨰 원소는 가장 큰 값이, right 의 첫번쨰 원소는 가장 작은 값이 위치
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-num, num))
    else:
        heapq.heappush(right_heap, (num, num))

    # 각 힙의 길이가 1보다 크고 크기를 비교하여 왼쪽값이 오른쪽 값보다 크면 자리를 바꿔줌
    if right_heap and left_heap[0][1] > right_heap[0][1]:
        left = heapq.heappop(left_heap)[1]
        right = heapq.heappop(right_heap)[1]

        heapq.heappush(left_heap, (-right, right))
        heapq.heappush(right_heap, (left, left))

    print(left_heap[0][1])

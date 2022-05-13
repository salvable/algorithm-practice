import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

testCase = int(input())

for _ in range(testCase):
    n = int(input())
    max_heap =[]
    min_heap = []
    check = [False] * n

    for i in range(n):
        oper = list(map(str, input().split()))
        # 연산이 입력연산일 경우
        if oper[0] == "I":
            # i 는 동기화 시켜주기 위한 장치
            heapq.heappush(max_heap, (-int(oper[1]), i))
            heapq.heappush(min_heap, (int(oper[1]), i))
            check[i] = True

        else:
            # 최대값 제거인경우
            if oper[1] == "1":
                # 최대 힙이 있고 최대값이 이미 제거상 상태라면 동기화를 위해 계속 제거
                while max_heap and check[max_heap[0][1]] == False:
                    heapq.heappop(max_heap)

                if max_heap:
                    check[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and check[min_heap[0][1]] == False:
                    heapq.heappop(min_heap)

                if min_heap:
                    check[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # check에서 True가 존재하지 않으면 모두 큐에서 제거된 상태므로 Empty출력
    if True not in check:
        print("Empty")
    else:
        # 제거되지 못한 것이 있다면 제거
        while max_heap and check[max_heap[0][1]] == False:
            heapq.heappop(max_heap)
        while min_heap and check[min_heap[0][1]] == False:
            heapq.heappop(min_heap)

        print(-max_heap[0][0], max_heap[0][0])
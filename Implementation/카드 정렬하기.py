def pythonTest():
    n 은 arr의 갯수
    n = 3
    # arr은 넘어오는 값
    arr = [10,20,40]
    heap = []
    result = 0

    for i in range(n):
        heapq.heappush(heap, arr[i])

    while len(heap) != 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        card_sum = first + second
        result += card_sum
        heapq.heappush(heap, card_sum)

    print(result)

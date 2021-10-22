def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 0
    while left <= right:
        blankCount = 0

        mid = (right + left) // 2

        # 순차적으로 돌면서 디딤돌이 0 이하인 것이 연속으로 k 개만큼 나오면 중지
        for stone in stones:
            if stone - mid <= 0:
                blankCount += 1
            else:
                blankCount = 0

            if blankCount >= k:
                break
       
        # k 개 이상 나오면 건너지 못하니 이를 정답에 기록하고 mid -1을 하여 더 적은값을 뺴었을때 답이 있는지 확인
        if blankCount < k:
            left = mid + 1 
        else:
            answer = mid
            right = mid - 1
    
    return answer

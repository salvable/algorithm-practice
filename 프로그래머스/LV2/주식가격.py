def solution(prices):
    answer = [0]*len(prices)
    stack = []
 
    for i, price in enumerate(prices):
        #stack에 인덱스 값을 저장해서 이전값과 현재 값을 비교 
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
 
        #떨어지지 않은 가격들을 answer에 추가
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
 
    return answer

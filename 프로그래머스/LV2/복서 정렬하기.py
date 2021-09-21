def solution(weights, head2head):
    answer = []
    
    for i in range(len(head2head)):
        win = 0
        lose = 0
        heavy_win = 0
        head2headList = list(head2head[i])
        for j in range(len(weights)):
            if head2headList[j] == "W":
                win += 1
                # 상대가 몸무게가 더 크면
                if weights[i] < weights[j]:
                    heavy_win += 1
            elif head2headList[j] == "L":
                lose += 1
        
        if win + lose != 0:
            answer.append([i+1, win/(win+lose), heavy_win, weights[i]])
        else:
            answer.append([i+1, 0, heavy_win, weights[i]])
    
    # 승률, 체급차 승리, 몸무게 순서로 sort
    answer.sort(reverse=True , key = lambda x : (x[1],x[2],x[3]))
    
    arr = []
    
    for i in answer:
        arr.append(i[0])
    return arr

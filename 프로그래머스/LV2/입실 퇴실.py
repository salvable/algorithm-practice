from collections import deque

def solution(enter, leave):
    answer = [0 for _ in range(len(enter)+1)]
    leave = deque(leave)
    area = []
    
    for i in enter:
        # 그 공간에 있는 사람들은 새로운 사람이 들어왔으니 1을 더해줌
        if len(area) != 0:
            for j in area:
                answer[j] += 1
        # 그 공간에 있는 사람의 수를 만난사람 수로 지정
        answer[i] += len(area)
        area.append(i)
        
        # leave의 0번째 인덱스가 area에 있으면 없애줌
        while leave and leave[0] in area:
            area.remove(leave.popleft())        

    return answer[1:]

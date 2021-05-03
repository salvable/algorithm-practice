def solution(record):
    answer = []
    log = []
    dic = dict()
    
    for i in record:
        split = i.split(" ")
            
        if split[0] == "Enter":
            dic[split[1]] = split[2]
            log.append([split[1], "님이 들어왔습니다."])
        elif split[0] == "Leave":
            log.append([split[1], "님이 나갔습니다."])
        elif split[0] == "Change":
            dic[split[1]] = split[2]

    for i in log:
        answer.append(dic[i[0]] + i[1])
    
    return answer

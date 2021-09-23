def solution(record):
    log = []
    dic = dict()
    
    for r in record:
        # 0번이 행동, 1번이 유저 아이디, 2번이 닉네임
        splitList = r.split(" ")
        
        if splitList[0] == "Enter":
            dic[splitList[1]] = splitList[2]
            log.append((splitList[0],splitList[1]))
        elif splitList[0] == "Leave":
            log.append((splitList[0],splitList[1]))
        elif splitList[0] == "Change":
            dic[splitList[1]] = splitList[2]
            log.append((splitList[0],splitList[1]))
            
    answer = []        
               
    for behavior, userId in log:
        if behavior == "Enter":
            answer.append(dic[userId] + "님이 들어왔습니다.")
        elif behavior == "Leave":
            answer.append(dic[userId] + "님이 나갔습니다.")
    
    return answer

def solution(s):
    arr = []
    answer = []
    # 숫자만 따로 골라냄
    s = s[2:-2].split("},{")
    
    for i in s:
        arr.append(i.split(","))
    
    arr.sort(key=len)
    
    for a in arr:
        for j in a:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer

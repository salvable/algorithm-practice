def solution(s):
    
    arr = []
    answer = []
    
    # {{ }}을 제거하기 위해 [2:-2], 숫자만 남기기 위해 split 을 두번 해줌
    for i in s[2:-2].split(("},{")):
        arr.append(i.split(","))
    
    arr.sort(key = len)   

    for i in arr:
        for j in  i:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer

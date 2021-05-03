def divide(s):
    # ( 개수 카운트
    count_L = 0
    # ) 개수 카운트
    count_R = 0
    
    for i in range(len(s)):
        if(s[i] == "("):
            count_L += 1
        elif(s[i]==")"):
            count_R += 1
        
        if count_L == count_R:
            return s[:i+1], s[i+1:]

def balance(u):
    stack = []
    
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            #스택에 (가 없을경우 False 리턴
            if not stack:
                return False
            stack.pop()
    
    # 정상적으로 for문을 모두 돈 경우 balance잡힌 문자열로 TRUE리턴
    return True        

def solution(p):
    answer = ''
    
    if p == "":
        return p

    u,v = divide(p)
    
    if(balance(u)):
        return u + solution(v)
    
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        
        for i in u[1:len(u)-1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
    
    return answer

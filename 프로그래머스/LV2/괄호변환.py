def balance(p):
    # 각각 (,) 의 개수
    count1 = 0
    count2 = 0
    
    for i in range(len(p)):
        if p[i] == "(":
            count1 += 1
        elif p[i] == ")":
            count2 += 1
            
        if count1 == count2:
            return (p[:i+1],p[i+1:])
        
def confirm(s):
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True

def solution(p):
    answer = ""
    
    # 1단계
    if len(p) == 0:
        return ""
    
    # 2단계
    u, v = balance(p)
    
    # 3단계
    if confirm(u):
        return u + solution(v)
    
    #4단계
    answer = "(" + solution(v) + ")"
    
    
    for i in u[1:-1]:
        if i == "(":
            answer += ")"
        else:
            answer += "("
    
    return answer

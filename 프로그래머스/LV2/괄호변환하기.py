from collections import deque

def solution(s):
    answer = 0
    #문자열을 밀기 위한 deque
    s_que = deque(s)
    
    #길이의 횟수만큼 미는것을 반복
    for i in range(len(s_que)):
        #괄호가 올바른가를 판단할 스택
        stack = [] 
        for j in s_que:
            if j == "[" or j == "{" or j == "(":
                stack.append(j)
            elif not stack:
                stack.append("#")
                break
            elif j == "]" and stack[-1] == "[":
                stack.pop()
            elif j == "}" and stack[-1] == "{":
                stack.pop()
            elif j == ")" and stack[-1] == "(":
                stack.pop()

        if len(stack) == 0:
            answer += 1
        
        s_que.append(s_que.popleft())
        
    return answer

from collections import deque

def solution(s):
    answer = 0
    q = deque(s)
    
    for _ in range(len(s)):
        stack = []
        
        for i in q:
            if i == "[" or i == "{" or i == "(":
                stack.append(i)
            # 첫번쨰 문자로 올바르지 않은 괄호가 들어왔을떄 예외처리    
            elif len(stack) == 0:
                stack.append("###")
            elif  i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            elif i == ")" and stack[-1] == "(":
                stack.pop()
                
        if len(stack) == 0:
            answer += 1
        
        q.append(q.popleft())
        
    return answer

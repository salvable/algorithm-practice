def solution(s):
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == "(":
            
            if i == "(":
                stack.append(i)
            else:
                stack.pop()
        else:
            break
            
    if(len(stack) == 0):
        return True

    return False

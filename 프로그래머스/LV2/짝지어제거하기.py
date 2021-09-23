def solution(s):
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif len(stack) != 0 and stack[-1] == i:
            stack.pop()
        elif len(stack) != 0 and stack[-1] != i:
            stack.append(i)
            
    # 스택이 비어있으면 모두 제거된 것이므로 -1 리턴
    if len(stack) == 0:
        return 1
    
    return 0

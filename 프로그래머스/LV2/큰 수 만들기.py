def solution(number, k):
    
    stack = [number[0]]
    
    # stack에 첫번쨰 값을 넣어놈
    for num in number[1:]:
        #스택 마지막 값이 num보다 작을경우 뺴서 버리고 새로운 값으로 대체 
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()        
        stack.append(num)
              
    if k != 0:
        stack = stack[:-k]
    
    return ''.join(stack)

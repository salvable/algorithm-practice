from collections import deque

def solution(s):
    answer = []
    for string in s :
        stack = []
        count = 0
        for s in string:
            
            # 문자열이 0이면
            if s == '0':
                
                # 앞에 2개가 1, 1인지 확인
                if stack[-2:] == ['1', '1']:
                    count += 1
                    stack.pop()
                    stack.pop()
                    
                # 앞에 2개가 1, 1이 아니면 그냥 0을 추가
                else:
                    stack.append(s)
                    
            # 문자열이 0이 아니면 그냥 추가
            else:
                stack.append(s)
        
        # 110이 없기 때문에 변화 불가능
        if count == 0:
            answer.append(string)
        
        # 110이 있다면
        else:
            final = deque()
            
            # 0이 나오기 전까지는 append
            while stack:
                if stack[-1] == '1':
                    final.append(stack.pop())
                elif stack[-1] == '0':
                    break
            
            # 0이 나왔다면 110을 주어진 count만큼 append
            while count > 0:
                final.appendleft('0')
                final.appendleft('1')
                final.appendleft('1')
                count -= 1
            
            # stack에 남아있는거 다 추가
            while stack:
                final.appendleft(stack.pop())
            answer.append(''.join(final))
    
    return answer

from itertools import permutations

def calculate(expression, op):
    expression_list = []
    tmp = ""
    
    for i in expression:
        if i.isdigit():
            tmp += i
        else:
            expression_list.append(tmp)
            tmp = ""
            expression_list.append(i)
    # 마지막 숫자 넣어주기
    expression_list.append(tmp)
    
    for o in op:
        stack = []
        while len(expression_list) > 0:
            tmp = expression_list.pop(0)
            if tmp == o:
                first = stack.pop()
                second = expression_list.pop(0)
                    
                if o == "+":
                    stack.append(str(int(first) + int(second)))
                if o == "-":
                    stack.append(str(int(first) - int(second)))
                if o == "*":
                    stack.append(str(int(first) * int(second)))
            else:
                stack.append(tmp)
        
        # 하나의 연산자가 돌고난 이후에 동기화 해줌
        expression_list = stack
    
    return abs(int(expression_list[0]))
    
    
def solution(expression):
    op = ["+","-","*"]
    op_List = list(permutations(op, 3))
    
    answer = []

    for i in op_List:
        answer.append(calculate(expression,i))
    
    return max(answer)

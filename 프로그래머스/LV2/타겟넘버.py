answer = 0 

def dfs(index,numbers,target,value):
    global answer
    number_length = len(numbers)
    
    # 끝에 도달하고 target값과 value 값이 같은경우
    if index == number_length and target == value:
        answer += 1
        return;
    
    # 끝에만 도달했을 경우
    if index == number_length:
        return;
    
    dfs(index+1,numbers,target,value+numbers[index])
    dfs(index+1,numbers,target,value-numbers[index])
    
def solution(numbers, target):
    global answer
    
    dfs(0,numbers,target,0)
    return answer

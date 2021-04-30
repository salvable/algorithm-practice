def solution(absolutes, signs):
    
    for i,sign in enumerate(signs):
        if(sign == False):
            absolutes[i] = -absolutes[i]
            
    answer = sum(absolutes)    
    
    return answer

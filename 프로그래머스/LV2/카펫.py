# x 가 가로 y가 세로의 길이일때 노란 카펫의길이는 x-2 , y-2

def solution(brown, yellow):
    answer = []  
    yellowArray = []
    
    for i in range(1,yellow+1):
        if(yellow % i == 0):
            yellowArray.append(i)
    
    for i in range(int(len(yellowArray)//2)+1):
        if((yellowArray[i]+2) * (yellowArray[-i-1]+2) - yellow == brown):
           answer.append(yellowArray[-i-1]+2)
           answer.append(yellowArray[i]+2)
           break
    
    return answer

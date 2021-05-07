def solution(arr):  
    # 0번 인덱스는 0의 개수, 1번 인덱스는 1의개수
    answer = [0] * 2
    
    #초기 x값, y값, r은 정사각형의 길이 
    def pressure(x,y,r):
        start = arr[x][y]
        for i in range(x,x+r):
            for j in range(y,y+r):
                if start != arr[i][j]:
                    # start값과 다르면 길이가 절반인 rr으로 pressure를 돌림 
                    rr = r // 2
                    pressure(x,y,rr)
                    pressure(x+rr,y,rr)
                    pressure(x,y+rr,rr)
                    pressure(x+rr,y+rr,rr)
                    return 
            
        #모두 값은 값이어서 정상일 경우 
        if arr[x][y] == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    
    
    # 0,0부터 시작
    pressure(0,0,len(arr))
            
    return answer

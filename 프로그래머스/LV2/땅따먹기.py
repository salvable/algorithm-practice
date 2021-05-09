def solution(land):
    answer = 0
    row = len(land)

    #행은 4로 고정
    #이전 행과 현재행을 더하는데 같은 열은 사용할수 없으므로 같은 열을 제외하고 탐색
    for i in range(row-1):
        land[i+1][0] = max(land[i][1],land[i][2],land[i][3]) + land[i+1][0]
        land[i+1][1] = max(land[i][0],land[i][2],land[i][3]) + land[i+1][1]        
        land[i+1][2] = max(land[i][0],land[i][1],land[i][3]) + land[i+1][2]
        land[i+1][3] = max(land[i][0],land[i][1],land[i][2]) + land[i+1][3]
    
    #마지막 행에서 가장 큰 값을 리턴
    return max(land[row-1][0],land[row-1][1],land[row-1][2],land[row-1][3])

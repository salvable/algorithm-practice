def solution(triangle):
    
    
    # 사이드는 각각의 첫번째, 마지막 원소에만 영향을 받고 나머지는 두값을 비교하여 큰값을 저장하여야 함
    
    # 행 접근 
    for i in range(1,len(triangle)):
        # 열의 개수는 행보다 항상 1이 많음
        for j in range(i+1):
            
            # 첫번째 원소일경우
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            # 마지막 원소일 경우
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            # 중간 값인경우 큰값을 넣어줘야 함
            else:
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
    
    # 마지막 줄의 최댓값 출력
    return max(triangle[-1])

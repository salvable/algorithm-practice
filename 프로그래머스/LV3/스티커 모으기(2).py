def solution(sticker):
    length = len(sticker)
    # 첫번째 스티커를 뗄때 마지막 인덱스는 떼지 않아야 하므로 첫번째를 뗄지 말지 2case로 나누어 접근
    
    # 스티커 갯수가 하나면 첫번째 값 리턴
    if length == 1:
        return sticker[0]
    
    # 첫번째 스티커를 떼는 경우
    dp1 = [0] * length
    
    # 첫번째를 무조건 떼므로 dp1[0]는 sticker의 첫번째 값, dp1[1]은 dp1[0]과 같은 값을 가짐 
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    
    for i in range(2, length-1):
        dp1[i] = max(dp1[i-2] + sticker[i], dp1[i-1])
    
    # 첫번째 스티커를 떼지 않는 경우
    dp2 = [0] * length
    # 첫번째 스티커를 떼지 않으므로 dp2[0]는 0 이되고 dp2[1]는 sticker의 두번째 값이 됨
    dp2[0] = 0
    dp2[1] = sticker[1]
    
    for i in range(2, length):
        dp2[i]= max(dp2[i-1], dp2[i-2] + sticker[i])
        
    return max(max(dp1),max(dp2))

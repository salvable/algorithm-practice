def solution(s):

    length = len(s)
    
    for i in range(1,length//2 +1):
        # count는 반복된 횟수 temp는 문자열을 이어붙이기 위한 임시공간 , pre 는 비교 대상이 될 문자열 
        count = 1 
        temp = ""
        pre = s[0:i]
        # i의 수만큼 건너 뛰며 체크
        for j in range(i,len(s),i):
            if pre == s[j:j+i]:
                count += 1
            else:
                if count >= 2:
                    temp += str(count) + pre
                else:
                    temp += pre
                # 이후 탐색을 위해 pre 재설정
                pre = s[j:j+i]
                count = 1
        if count >= 2:
            temp += str(count) + pre
        else:
            temp += pre    
        
        length = min(length, len(temp))
            
    return length

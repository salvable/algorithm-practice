# 문자열 압축

#줄일수 있는 최대한도는 문자열의 절반 

def solution(s):
    length = len(s)
    
    # 문자열을 1부터 절반까지 줄일수 있는 범위를 확인 할 것
    for i in range(1,length // 2 + 1):
        #중복되는 문자의 개수를 기록할 count와 문자열 tmp
        count = 1
        tmp = ""
        pre = s[0:i]
        
        for j in range(i,len(s),i):
            if pre == s[j:j+i]:
                count += 1
            else:
                if count >= 2:
                    tmp += str(count) + pre
                else:
                    tmp += pre
                #이후 탐색을 위해 재설정
                pre = s[j:j+i]
                count = 1
        # 나머지 문자열에 대한 처리
        if count >= 2:
            tmp += str(count) + pre
        else:
            tmp += pre       
        length = min(length,len(tmp))
    return length

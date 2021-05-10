# n은 진법, number는 숫자, 각 진법별로 나누어서 리턴해줌
# 시행착오1 // 2,8,10,16 뿐만 아니라 3,4,5... 진법도 테스트 케이스에 있는듯함
# 해당 진법 변환 코드는 구글링 해서 긁어옴
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    arr = [] 
    answer = ""
    number = 0
    
    # arr이 튜브가 구하고자 하는 값까지만 돌도록 설정
    # 0부터 1씩 증가하면서 변환한 값들을 리스트로 변환해서 arr에 추가해줌
    while len(arr) < t * m:
        arr += list(convert(number,n))
        number += 1
    
    for i in range(t):
        answer += arr[i*m + p -1]
    answer = answer.upper()
    
    return answer

def solution(s):
    answer = list(map(int, s.split(" ")))
    
    maxNumber = max(answer)
    minNumber = min(answer)

    return str(minNumber) + " " + str(maxNumber)
'

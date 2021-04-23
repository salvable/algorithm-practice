def solution(numbers):
    
    arr = list(map(str,numbers))
    
    arr.sort(key = lambda x : x*3, reverse = True)

    # numbers의 모든 원소가 0 일 경우 str이면 0000을 출력 하기에 int로 형변환 후 다시 str로 형변환
    return str(int(''.join(arr)))

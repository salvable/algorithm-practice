def solution(numbers):
    answer = []
    # 문자열로 정리하면 사전순으로 정리되는데 reverse옵션을 붙이면 9 부터 시작되므로 가장 큰 수를 만들 수 있음
    for i in numbers:
        answer.append(str(i))
    
    # number의 원소는 1 부터 1000 까지이므로 문자열을 3배로 증가시켜 비교하도록 함
    answer.sort(reverse=True, key = lambda x : x * 3)
    
    return str(int("".join(answer)))

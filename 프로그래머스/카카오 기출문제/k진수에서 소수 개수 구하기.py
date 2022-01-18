import math


# n 진법 변환 함수
def convert(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

# 소수인지 판별하는 함수
def isPrime(n):
    result = True

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = False
            break

    return result


def solution(n, k):
    answer = 0
    temp = str(convert(n, k))
    arr = temp.split("0")

    for i in arr:
        # 1보다 작거나 공백이면 패스
        if i == "" or int(i) < 2:
            continue

        # 소수라면 answer + 1
        if isPrime(int(i)):
            answer += 1

    return answer
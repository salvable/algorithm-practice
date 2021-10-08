def prime_list(N):
    # 에라토스테네스의 체
    prime = [True] * (N + 1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int((N + 1) ** 0.5)

    for i in range(2, m + 1):
        if prime[i] == True:  # i가 소수인 경우
            for j in range(i + i, N + 1, i):  # i이후 i의 배수들을 False로 판정
                prime[j] = False

    return [i for i in range(2, N + 1) if prime[i] == True]


N = int(input())
primes = prime_list(N)
start, end, count = 0, 0, 0

while end < len(primes):
    temp = sum(primes[start:end+1])

    if temp == N:
        count += 1
        start += 1

    elif temp < N:
        end += 1
    else:
        start += 1

print(count)

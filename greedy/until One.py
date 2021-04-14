# 입력받은 N이 1이 될 떄까지 다음의 두 과정 중 하나를 반복적으로 수행
# 단, 두번쨰 연산은 N이 K로 나우어 떨어질때만 선택 가능
# 1. N에서 1을 뺸다.
# 2. N을 K로 나눈다.

# 1을 만드는 최소 횟수를 구하라

n,k = map(int, input().split())

number = 0

while(n != 1):
    if(n % k == 0):
        n /= k
        number += 1
    else:
        n -= 1
        number += 1

print(number)

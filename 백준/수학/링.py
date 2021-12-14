import math

n = int(input())

arr = list(map(int, input().split()))

# 첫번째 원을 저장할 변수
circle = arr[0]

for i in range(1,len(arr)):
    # 최대공약수를 구한 뒤 각각의 값을 최대공약수로 나눈 값을 string으로 나누어 출력
    x = math.gcd(circle,arr[i])

    print(str(circle//x) + "/" + str(arr[i]//x))

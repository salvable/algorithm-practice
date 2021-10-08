import sys

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0, 0 
sum = 0 # 
length = 1e9 

while True:
    # 만약 총 합이 S가 넘는다면, sum에서 number[left]의 값을 빼고 카운트를 하나 올림
    if sum >= S:
        print(right,left)
        length = min(length, right - left)
        sum -= numbers[left]
        left += 1

    # 인덱스 최고 처리
    elif right == N:
        break

    else:
        sum += numbers[right]
        print(sum)
        right += 1

if length == sys.maxsize:
    print(0)
else:
    print(length)

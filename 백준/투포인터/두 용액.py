import sys

input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))

start = 0
end = n-1

# 0으로 부터 떨어진 값
abs_zero = abs(arr[start] + arr[end])
abs_start = start
abs_end = end

while start < end:
    tmp = arr[start] + arr[end]

    # 만약 tmp 절댓값이 0에 더 가까우면
    if abs(tmp) < abs_zero:
        abs_zero = abs(tmp)
        abs_start = start
        abs_end = end

    # tmp값이 양수면 end index를 하나 땡기고 반대일경우 start를 하나 올림
    if tmp > 0:
        end -= 1
    else:
        start += 1

print(arr[abs_start],arr[abs_end])

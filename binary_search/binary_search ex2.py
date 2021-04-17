n, m = map(int, input().split())

array = list(map(int, input().split()))

start = 0

# 리스트의 원소중 제일 긴것을 기준으로 설정
end = max(array)


result = 0
while(start <= end):

    # total은 m의 값이 나와야 함
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid +1

print(result)

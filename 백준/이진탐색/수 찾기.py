N = int(input())
arr1 = list(map(int,input().split()))
arr1.sort()

# 찾고자 하는 수들
M = int(input())
arr2 = list(map(int,input().split()))

for i in arr2:
    start = 0
    end = N-1
    target = i

    answer = 0

    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == target:
            # 값을 찾으면 1로 바꿔줌
            answer = 1
            break
        elif arr1[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    print(answer)

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    sum = 0

    for i in tree:
        if i > mid:
            sum += i - mid

#start 와 sum 은 비례
    if sum < M:
        end = mid -1
    else:
        start = mid + 1

print(end)

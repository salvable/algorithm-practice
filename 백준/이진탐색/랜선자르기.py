import sys

K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
# 최소 값은 1, 최댓값은 가지고 있는 랜선중 가장 긴 길이
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    # 중간값을 가지고 만들 랜선의 숫자
    line = 0

    for i in lan:
        # 길이를 mid값으로 나눈 몫 만큼 랜선을 추가해줌
        line += i // mid

    if line < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)

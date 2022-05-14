import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
# 누적합으로 이용할 리스트
sum_arr = [0]

for i in range(len(arr)):
    sum_arr.append(arr[i] + sum_arr[i])

for _ in range(m):
    start, end = map(int, input().split())

    print(sum_arr[end] - sum_arr[start-1])
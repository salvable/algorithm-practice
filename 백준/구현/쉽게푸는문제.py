import sys

input = sys.stdin.readline  # 빠른 입출력 위한 코드


a,b = map(int, input().split())

arr = [0]
index = 1

while len(arr) <= 1000:
    for i in range(index):
        arr.append(index)

    index += 1

print(sum(arr[a:b+1]))
N = int(input())
arr = list(map(int, input().split()))

arr.sort()

time = 0
result = 0

for i in arr:
    time += i
    result += time

print(result)

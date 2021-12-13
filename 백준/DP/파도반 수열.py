n = int(input())

arr = [1,1,1,2,2]

# 5 ~ 100
for i in range(5,100):
    arr.append(arr[i-5] + arr[i-1])

for _ in range(n):
    k = int(input())
    print(arr[k-1])

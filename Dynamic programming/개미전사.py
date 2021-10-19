# 인접한 배열의 행은 털수 없음, 식량의 최댓값 구하기
n = int(input())

array = list(map(int,input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(d[0],array[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])

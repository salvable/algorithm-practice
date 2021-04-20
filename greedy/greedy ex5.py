#서로 다른 무게의 볼링공 경우의 수, 최대무게 10

n,m = map(int, input().split())

data = list(map(int, input().split()))

#1부터 10까지의 볼링공 카운트 배열
array = [0] * 10

for i in data:
    array[i] += 1

answer = 0


#무게가 1부터 m까지인 볼링공에 대하여
for i in range(1,m+1):
    n -= array[i]
    answer += array[i] * n

print(answer)

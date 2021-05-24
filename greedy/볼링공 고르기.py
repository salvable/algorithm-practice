n , m = map(int, input().split())
data = list(map(int,input().split()))

# 공의 무게는 최대 10이므로 배열로 공의 무게에 대한 공의 갯수를 파악한다.

ball = [0] * 11

for i in data:
    ball[i] += 1

answer = 0

# n - ball[i] 를 통해 해당 무게가 아닌 볼을 골라내어 곱한값을 answer에 추가

for i in range(1,m+1):
    n -= ball[i]
    answer += n * ball[i]

print(answer)
    

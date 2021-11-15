n = int(input())
d = [0] * (n + 1)

for i in range(2,n+1):
    # 1을 뺴는 경우
    d[i] = d[i-1] + 1

    # 2로 나눠지는 경우 d[i//2]에 +1 된 값을 가지므로 이거에 +1 한 값이 횟수가 되므로 최솟값과 비교
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2] + 1)
    # 2와 같음
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3] + 1)

print(d[n])

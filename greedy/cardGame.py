n,m = map(int, input().split())

answer = 0

for i in range(n):
    data = list(map(int, input().split()))

    mindata = min(data)
    answer = max(mindata,answer)

print(answer)

N = int(input())
conf = []

for _ in range(N):
    start, end = map(int, input().split())
    conf.append([start, end])


conf = sorted(conf, key=lambda x: (x[1], x[0]))

end = 0
count = 0

# x,y는 시작시간, 종료시간
for x, y in conf:
    # 시작시간이 종료시간보다 크다면
    if end <= x:
        count += 1
        end = y

print(count)

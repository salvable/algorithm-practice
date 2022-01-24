N = int(input())
M = int(input())

arr = list(map(int, input().split()))

result = abs(100 - N)

# 채널 자체는 무한대이므로 범위는 1000001 로 설정
for i in range(1000001):
    string = str(i)

    for j in range(len(string)):
        # 고장난 키가 있으면
        if int(string[j]) in arr:
            break

        # 문자 끝까지 고장난 버튼이 포함되지 않았다면
        elif j == len(string) - 1:
            result = min(result, len(string) + abs(int(string)-N))

print(result)
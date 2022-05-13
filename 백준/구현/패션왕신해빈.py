import sys
input = sys.stdin.readline

testCase = int(input())

for _ in range(testCase):
    n = int(input())

    dic = dict()

    for _ in range(n):
        # 0은 의상 1은 의상부위
        arr = list(map(str, input().split()))

        if arr[1] not in dic.keys():
            # 벗고 있는 경우와 최초 첫 옷을 세어 2가지 경우
            dic[arr[1]] = 2

        else:
            dic[arr[1]] += 1

    answer = 1

    for i in dic.values():
        answer *= i

    # 둘다 벗고 있는 경우를 제외하기 위한 -1
    print(answer - 1)
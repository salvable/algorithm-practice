n = int(input())
arr = list(map(int, input().split()))

B, C = map(int, input().split())

answer = 0

for i in range(n):
    # 시험장을 돌며 총 감독관이 감독할 수 있는 학생 수만큼 빼어 answer에 더해줌
    if arr[i] > 0:
        arr[i] -= B
        answer += 1

    # 이후 남은 인원을 부 감독관이 관리할 수 있는 수만큼 나누어 추가해줌

    if arr[i] > 0:
        answer += arr[i] // C
        # 나머지가 있을경우 감독관 한명을 추가
        if arr[i] % C != 0:
            answer += 1

print(answer)


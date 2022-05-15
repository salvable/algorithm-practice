import sys
input = sys.stdin.readline


n, m = map(int, input().split())
# 진실을 아는 사람의 set
know = set(input().split()[1:])
party = []

for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for p in party:
        # 각 set끼리 교집합 연산하여 있으면 합집합으로 추가
        if p & know:
            know = know.union(p)

answer = 0

for p in party:
    if p & know:
        continue

    answer += 1

print(answer)

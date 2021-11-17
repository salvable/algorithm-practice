from itertools import combinations

arr = [int(input()) for i in range(9)]

combination = list(combinations(arr,7))

for i in combination:
    if sum(i) == 100:
        arr = i
        break

answer = []

for i in arr:
    answer.append(i)

answer.sort()

for i in answer:
    print(i)

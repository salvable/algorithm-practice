from itertools import combinations, permutations, combinations_with_replacement

n = int(input())
arr = list(map(int, input().split()))

cases = list(permutations(arr))

result = -1e9

for case in cases:
    case_sum = 0

    for i in range(len(case) - 1):
        case_sum += abs(case[i] - case[i+1])

    result = max(result,case_sum)

print(result)

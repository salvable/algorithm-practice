from itertools import combinations, permutations


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

# n 의 절반으로 팀을 나누기 때문에 0 ~ n
comb_arr = [i for i in range(n)]

combination = list(combinations(comb_arr, n // 2))

min_value = 1e9

for comb in combination:
    start = 0
    link = 0

    for x in comb:
        for y in comb:
            if x != y:
                start += arr[x][y]

    # comb 에 해당하지 않는 팀으로 구성되는 link_arr 생성
    link_arr = [i for i in range(n) if i not in comb]
    for x in link_arr:
        for y in link_arr:
            if x != y:
                link += arr[x][y]

    min_value = min(min_value, abs(start - link))

print(min_value)

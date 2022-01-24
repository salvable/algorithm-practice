from itertools import combinations, permutations

L,C = map(int, input().split())

arr = sorted(input().split())

vowel = ["a", "e", "i", "o", "u"]

comb = list(combinations(arr, L))

for c in comb:
    # 각각은 자음 모음 카운트
    count_v = 0
    count_c = 0

    for i in c:
        if i in vowel:
            count_v += 1
        else:
            count_c += 1

    if count_v >=1 and count_c >=2:
        print("".join(c))
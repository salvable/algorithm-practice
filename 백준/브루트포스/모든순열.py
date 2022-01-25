from itertools import combinations, permutations, combinations_with_replacement

n = int(input())
arr = [i+1 for i in range(n)]


cases = list(permutations(arr))

for case in cases:

    for i in case:
        print(i, end=" ")
    print("")
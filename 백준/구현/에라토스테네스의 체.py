import sys

input = sys.stdin.readline  # 빠른 입출력 위한 코드

n, k = map(int, input().split())

# index 0 ~ 1000
prime = [True,True] + [True] * (n-1)
count = 0
flag = False

for i in range(2,len(prime)+1):
    for j in range(i,n+1,i):
        if prime[j]:
            prime[j] = False
            count += 1

        if count == k:
            flag = True
            print(j)
            break

    if flag:
        break

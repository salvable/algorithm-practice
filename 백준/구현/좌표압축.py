import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
dic = dict()

arr = list(map(int, input().split()))

sort_setArr = sorted(set(arr))

# 정렬된 sort_setArr 과 i 로  몇개보다 작은지 카운팅
for i in range(len(sort_setArr)):
    dic[sort_setArr[i]] = i

for i in arr:
    print(dic[i], end=" ")
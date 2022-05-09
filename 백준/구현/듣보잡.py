import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

dic = dict()
arr = []
for i in range(n):
    dic[str(input().strip())] = True

for i in range(m):
    key = str(input().strip())
    if key in dic.keys():
        arr.append(key)

arr.sort()

print(len(arr))

for i in range(len(arr)):
    print(arr[i])

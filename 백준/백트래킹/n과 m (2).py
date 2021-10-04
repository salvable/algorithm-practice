n,m = list(map(int,input().split()))

arr = []

def dfs(s):
    if len(arr) == m:
        print(" ".join(map(str,arr)))
     
    for i in range(s,n+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()
# 1부터 시작
dfs(1)

def find(parent,x):
    if parent[x] != x:
        return find(parent,parent[x])

    return parent[x]

def union(parent, x, y):
    a = find(parent,x)
    b = find(parent,y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

for i in range(1,n+1):
    arr = list(map(int,input().split()))

    for j in range(1, len(arr)+1):
        # 연결되어 있으면 union처리
        if arr[j-1] == 1:
            union(parent, i, j)

plan = list(map(int, input().split()))

result = []

for i in plan:
    result.append(find(parent, i))

# 중복되는 루트노드가 1개라면 모두 이어져 있으므로 여행이 가능
if len(set(result)) == 1:
    print("YES")
else:
    print("NO")
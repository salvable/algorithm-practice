import math

n = int(input())
parent = [i for i in range(n+1)]

star = []
edge = []

for _ in range(n):
    x, y = map(float, input().split())
    star.append((x,y))

# 점들의 사이 거리를 모두 계산하여 간선 배열에 저장한뒤 길이가 짧은 순으로 정렬
for i in range(n-1):
    for j in range(i+1, n):
        edge.append(((math.sqrt((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2), i, j)))

edge.sort()

def find(parent,x):
    if parent[x] != x:
        return find(parent,parent[x])

    return parent[x]

def union(parent,x,y):
    a = find(parent, x)
    b = find(parent, y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


result = 0

for e in edge:
    cost, x, y = e

    # 루트노드가 같을경우 잇게되면 사이클이 생기게 되므로 같지 않을 경우에만 이어줌
    if find(parent,x) != find(parent,y):
        union(parent,x,y)
        result += cost

print(round(result,2))
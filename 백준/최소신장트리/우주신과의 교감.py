import math

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

location = []
edge = []


def find(parent, x):
    if parent[x] != x:
        return find(parent,parent[x])

    return parent[x]


def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(n):
    x, y = map(int, input().split())
    location.append((x, y))

# 이미 연결되어 있는 것들 union 으로 연결
for _ in range(m):
    x, y = map(int, input().split())
    union(parent, x-1, y-1)

# 점들의 사이 거리를 모두 계산하여 간선 배열에 저장한뒤 길이가 짧은 순으로 정렬
for i in range(n-1):
    for j in range(i+1, n):
        edge.append(((math.sqrt((location[i][0] - location[j][0])**2 + (location[i][1] - location[j][1])**2), i, j)))

edge.sort()
result = 0

for e in edge:
    cost, x, y = e

    # 루트노드가 같을경우 잇게되면 사이클이 생기게 되므로 같지 않을 경우에만 이어줌
    if find(parent,x) != find(parent,y):
        union(parent,x,y)
        result += cost

print('%.2f' %(result))
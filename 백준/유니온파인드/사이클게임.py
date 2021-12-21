def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])

    return x

def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
parent = [i for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())

    # 입력받은 두 수의 루트 노드가 같을경우 연결시 사이클이 생기므로 출력하고 break
    if find(parent,x) == find(parent,y):
        print(i+1)
        break

    union(parent, x, y)

else:
    print(0)

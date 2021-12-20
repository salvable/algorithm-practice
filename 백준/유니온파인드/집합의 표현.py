import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

# 특정 원소가 속한 집합 찾기
def find(parent, x):
    if parent[x] != x:
        return find(parent,parent[x])

    # 재귀로 루트 노드를 찾았다면 리턴
    return x

def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:
        union(parent, a, b)
    else:
        if find(parent,a) == find(parent,b):
            print("YES")
        else:
            print("NO")
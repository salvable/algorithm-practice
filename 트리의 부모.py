from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
visit = [-1] * (n + 1)
parent = [[] for _ in range(n + 1)]


for _ in range(n - 1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def bfs(root):
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()

        for next_node in graph[node]:
            # 부모리스트에 추가해줌
            if visit[next_node] == -1:
                visit[next_node] = 1
                parent[next_node].append(node)
                q.append(next_node)

    return parent

bfs(1)

for i in parent[2:]:
    print(i[0])

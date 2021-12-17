from collections import deque

n = int(input())
# 연결정보를 기록할 graph와 부모정보를 기록할 parent, 방문정보를 기록할 visited
graph = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()

        # 해당 노드와 연결된 노드를 탐색
        for next_node in graph[node]:
            # 연결된 노드가 방문한 적이 없다면
            if visited[next_node] == -1:
                # 방문처리, 부모 추가, 큐에 삽입
                visited[next_node] = 1
                parent[next_node].append(node)
                q.append(next_node)

bfs(1)

for i in parent[2:]:
    print(i[0])

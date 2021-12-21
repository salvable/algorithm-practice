from collections import deque

TC = int(input())

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 1
    cnt = 0

    while q:
        now = q.popleft()

        for next_node in graph[now]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                cnt += 1
                q.append(next_node)

    return cnt

for _ in range(TC):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = 0

    for i in range(1,n+1):
        # 방문하지 않은 경우에만
        if visited[i] == 0:
            answer += bfs(i)

    print(answer)
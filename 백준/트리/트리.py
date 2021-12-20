from collections import deque

case = 0

# 트리인지 아닌지 사이클을 확인하는 함수
def bfs(node):
    result = True
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        # 해당 node가 방문되었는지 확인, 방문 되었으면 사이클이 돈 것
        if visited[node] == 1:
            result = False

        visited[node] = 1

        for next_node in graph[node]:
            # 미방문 노드만 방문
            if visited[next_node] == 0:
                q.append(next_node)
    return result

while True:
    case += 1

    # 정점의 개수 n과 간선의 개수 m
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    tree = 0

    # 각 노드 기준으로 탐색할 것인데
    for i in range(1,n+1):
        # 방문한적이 없는 노드만 탐색
        if visited[i] == 0:
            # 사이클을 형성하지 않는다면
            if bfs(i):
                tree += 1

    if tree > 1:
        print("Case " + str(case) + ": A forest of " + str(tree) + " trees.")
    elif tree == 1:
        print("Case " + str(case) + ": There is one tree.")
    else:
        print("Case " + str(case) + ": No trees.")
from collections import deque
import sys
input = sys.stdin.readline


def topology():
    dp = [0] * (n + 1)
    q = deque()

    for i in range(1, n+1):
        # 해당 진입 차수가 0이라면 큐에 넣어줌
        if in_degree[i] == 0:
            q.append(i)
            dp[i] += time[i]

    while q:
        now = q.popleft()

        # 해당 노드와 연결된 노드들을 돌며 진입차수를 1씩 낮추고 진입차수가 0이 된다면 큐에 넣어줌
        for i in graph[now]:
            in_degree[i] -= 1
            # 더 오래 걸리는 값을 가져야 함
            dp[i] = max(dp[i], dp[now] + time[i])

            if in_degree[i] == 0:
                q.append(i)

    return dp[target]


test = int(input())

for t in range(test):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    # 진입차수
    in_degree = [0] * (n + 1)

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    target = int(input())

    print(topology())
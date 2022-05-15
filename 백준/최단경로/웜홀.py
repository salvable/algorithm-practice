import sys


def BF():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for cost, node in graph[j]:
                if distance[node] > cost + distance[j]:
                    distance[node] = cost + distance[j]
                    if i == n:
                        return False
    return True


testCase = int(input())

for _ in range(testCase):
    n, m, w = map(int, input().split())
    distance = [1e9 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, cost = map(int, input().split())

        graph[a].append((cost, b))
        graph[b].append((cost, a))

    for _ in range(w):
        a, b, cost = map(int, input().split())

        graph[a].append((-cost, b))

    result = BF()

    print("No" if result else "YES")
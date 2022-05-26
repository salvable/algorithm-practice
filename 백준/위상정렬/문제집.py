import heapq
import sys
input = sys.stdin.readline


def topology():
    q = []
    result = []

    for index in range(1, n+1):
        if in_degree[index] == 0:
            heapq.heappush(q, index)

    while q:
        now = heapq.heappop(q)
        result.append(now)

        for next_question in graph[now]:
            in_degree[next_question] -= 1
            if in_degree[next_question] == 0:
                heapq.heappush(q, next_question)

    return result


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    in_degree[y] += 1

answer = topology()

print(" ".join(map(str, answer)))
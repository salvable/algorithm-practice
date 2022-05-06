import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[1e9] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = [1e9]

for i in graph[1:]:
    result.append(sum(i[1:]))

for i in range(len(result)):
    if result[i] == min(result):
        print(i)
        break
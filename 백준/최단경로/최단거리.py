import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j]):
                graph[i][j] = 1

# arr 리스트의 값의 형이 int 형이라 join 으로 붙이기 불가능해서 2중 for문 사용
for arr in graph:
    for i in arr:
        print(i , end= " ")
    print("")
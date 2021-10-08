import sys
from collections import Counter
INF = int(1e9)
from collections import deque

input = sys.stdin.readline
k = int(input())

def bfs(start):
    visit[start] = 1
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] = -visit[x]
                q.append(i)
            else:
                if visit[i] == visit[x]:
                    return False
    return True

for i in range(k):
    v, e = map(int, input().split())
    isTrue = True
    graph = [[] for i in range(v + 1)]
    visit = [0] * (v+1)
    flag = 1
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for k in range(1, v + 1):
        if visit[k] == 0:
            if not bfs(k):
                flag = -1
                break

    if flag == 1:
        print("YES")
    else:
        print("NO")

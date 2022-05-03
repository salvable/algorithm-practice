import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
edges = []

dist = [1e9] * (n+1)

for _ in range(m):
    x, y, d = map(int, input().split())
    edges.append((x, y, d))

# 음수 간선이 존재하므로 벨만 포드 알고리즘을 활용
def bf(start):
    dist[start] = 0

    for i in range(n):
        for j in range(m):
            current_node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 출발하는 노드값이 1e9가 아니고 도착 노드의 비용이 현재노드 + 비용보다 클때 작은 값으로 초기화 해줌
            if dist[current_node] != 1e9 and dist[next_node] > dist[current_node] + cost:
                dist[next_node] = dist[current_node] + cost
                # n번째 라운드에서도 값이 갱신되면 음수 순환이 존재하는 것
                if i == n - 1:
                    return True
    # 사이클이 발견 되지 않았으므로 False 리턴
    return False


result = bf(1)

if result:
    print("-1")

else:

    for i in range(2,n+1):
        # dist의 값이 1e9면 도착할 수 없으므로 -1
        if dist[i] == 1e9:
            print("-1")
        else:
            print(dist[i])
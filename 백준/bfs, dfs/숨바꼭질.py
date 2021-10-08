from collections import deque

n, k = map(int, input().split())
dist = [0] * 100001

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            break

        for nx in (x-1,x+1,x * 2):
            if 0 <= nx < 100001 and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)

bfs()

print(dist[k])

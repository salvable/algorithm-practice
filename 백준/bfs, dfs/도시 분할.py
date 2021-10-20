from collections import deque

# 땅의 크기 n , 이동하기 위한 최소, 최대 차이
n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

def process(x,y,index):
   united = []
   united.append((x,y))
   q = deque()
   q.append((x,y))
   # 그룹은 매김
   union[x][y] = index
   # 현재 인구수
   summary = graph[x][y]
   # 연합 국가의 수
   count = 1

   while q:
       x,y = q.popleft()

       for i in range(4):
           nx = x + dx[i]
           ny = y + dy[i]

           # 아무 소속도 아닐 떄 추가
           if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
               # 인구 차이가 설정된 인구차이 최소, 최대를 만족 할 때
               if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                   q.append((nx,ny))
                   union[nx][ny] = index
                   summary += graph[nx][ny]
                   count += 1
                   united.append((nx,ny))

   # 인구 배분하기
   for i,j in united:
       graph[i][j] = summary // count
   return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j,index)
                index += 1
    if index == n * n:
        break
    total_count += 1

print(total_count)

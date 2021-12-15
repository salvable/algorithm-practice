from collections import deque

n = int(input())
q = deque()

for i in range(1,n+1):
    q.append(i)

# left 가 카드 위 right 가 아래

while len(q) != 1:
    # 제일 위 카드를 버림
    q.popleft()

    # 제일 위에 있는 카드를 제일 아래로 내림
    temp = q.popleft()
    q.append(temp)

print(q[0])

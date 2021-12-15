import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == "push_front":
        q.appendleft(command[1])
    elif command[0] == "push_back":
        q.append(command[1])
    elif command[0] == "pop_front":
        if len(q) != 0:
            print(q.popleft())
        else:
            print("-1")
    elif command[0] == "pop_back":
        if len(q) != 0:
            print(q.pop())
        else:
            print("-1")
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if q:
            print(q[0])
        else:
            print("-1")

    elif command[0] == "back":
        if q:
            print(q[-1])
        else:
            print("-1")


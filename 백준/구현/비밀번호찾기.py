import sys
input = sys.stdin.readline


n, m = map(int, input().split())

storage = dict()

for _ in range(n):
    target, password = map(str, input().split())

    storage[target] = password

for _ in range(m):
    target = str(input().strip())
    print(storage[target])
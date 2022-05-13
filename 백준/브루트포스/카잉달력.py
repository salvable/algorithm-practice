import sys

input = sys.stdin.readline

testCase = int(input())

for _ in range(testCase):
    m, n, x, y = map(int, input().split())

    # 최대범위는 m*n을 넘을수 없기 때문에
    while x <= m * n:

        if (x - 1) % n + 1 == y:
            break

        x += m

    print(x if x <= m * n else -1)


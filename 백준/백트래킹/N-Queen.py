import sys
input = sys.stdin.readline


def confirm(x):
    for i in range(x):
        # 같은 열에 있거나 대각선에 있으면 False
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == x - i:
            return False

    return True

def dfs(x):
    global answer

    if x == n:
        answer += 1
    else:
        for i in range(n):
            queen[x] = i
            # 확인하여 퀸을 놓을 수 있으면
            if confirm(x):
                dfs(x + 1)

n = int(input())
queen = [0] * n
answer = 0

dfs(0)

print(answer)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


str = list(input().rstrip())
bomb = list(input().rstrip())
stack = []

for i in range(len(str)):
    stack.append(str[i])

    # 스택의 마지막 글자가 폭탄문자열의 마지막 문자와 같고 스택이 더 길경우에 터질 가능성이 있으므로
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        # 만약 bomb와 문자열이 같다면
        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
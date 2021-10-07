import sys

commands = sys.stdin.readlines()

for command in commands[:-1]:
    stack = []
    # 한글자 씩 돌며
    for t in command:
        if t == "(" or t == "[":
            stack.append(t)
        elif t == "]":
            if not stack or stack.pop() != '[':
                print('no')
                break
        elif t == ')':
            if not stack or stack.pop() != '(':
                print('no')
                break
        elif t == '.':
            if stack:
                print('no')
            else:
                print("yes")

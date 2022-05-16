import sys
input = sys.stdin.readline

string = list(input())
stack = []
answer = ""

for s in string:
    # 알파벳이면 넣어줌
    if s.isalpha():
        answer += s

    else:
        if s == "(":
            stack.append(s)

        # 우선 순위에 따라 같은 우선순위가 나오면 계속해서 넣어줌
        elif s == "*" or s == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(s)
        # +, - 보다 우선순위가 낮은 것은 없으므로 새로 괄호를 열지 않는 이상 계속해서 추가
        elif s == "+" or s == "-":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.append(s)
        # 괄호를 닫으면 열린 괄호가 없을때 까지 빼냄
        elif s == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()

while stack:
    answer += stack.pop()

print(answer)
import sys

m = int(sys.stdin.readline())

# 중복을 방지하기 위해 배열보다 set을 선택
arr = [0] * 21

for _ in range(m):
    oper = sys.stdin.readline().strip().split()

    if len(oper) == 1:
        if oper[0] == "all":
            arr = [1] * 21
        #empty 처리
        else:
            arr = [0] * 21

    else:
        number = int(oper[1])

        if oper[0] == "add" and arr[number] == 0:
            arr[number] = 1
        elif oper[0] == "remove" and arr[number] == 1:
            arr[number] = 0
        elif oper[0] == "check":
            if arr[number] == 1:
                print(1)
            else:
                print(0)
        elif oper[0] == "toggle":
            if arr[number] == 1:
                arr[number] = 0
            else:
                arr[number] = 1

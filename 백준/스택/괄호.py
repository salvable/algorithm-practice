n = int(input())

for _ in range(n):
    string = input()
    check = 0
    for s in string:
        if s == "(":
            check += 1
        elif s == ")":
            check -= 1

        if check < 0:
            print("NO")
            break

    if check > 0:
        print("NO")
    if check == 0:
        print("YES")


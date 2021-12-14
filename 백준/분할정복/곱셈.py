a, b, c = map(int, input().split(" "))

def divide(x,y):
    if y == 1:
        return a % c
    else:
        temp = divide(x, y // 2)

        # 각각은 짝수, 홀수일때
        if y % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * x) % c
print(divide(a, b))

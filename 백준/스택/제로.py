n = int(input())
stack = []

for _ in range(n):
    string = input()

    for s in string:
        print(s)

    
print(sum(stack))

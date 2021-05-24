# 구현
# 무조건 짝수 자리수로 주어짐

n = input()

mid = int(len(n) / 2)

pre = list(n[:mid])
after = list(n[mid:])

print(pre, after)
answer = 0

for i in range(len(pre)):
    diff = int(pre[i]) - int(after[i])
    answer += diff

if answer != 0:
    print("READY")
else:
    print("Lucky")

a = input()

a = a.split("-")


for i in range(len(a)):
    if "+" in a[i]:
        sum = 0
        plus = a[i].split("+")
        for j in plus:
            sum += int(j)
        a[i] = int(sum)


answer = int(a[0])

for i in range(1,len(a)):
    answer -= int(a[i])

print(answer)

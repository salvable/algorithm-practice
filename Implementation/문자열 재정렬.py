#구현

data = input()

alpha = []
number = 0

for x in data:

    if x.isalpha():
        alpha.append(x)
    else:
        number += int(x)

alpha.sort()
alpha.append(str(number))

result = "".join(alpha)


print(result)

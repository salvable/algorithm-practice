data = input()

# 0과 1 카운트
zeroCount = 0

oneCount = 0

# 1들을 0으로 바꾸는 경우와 0을 1로 바꾸는 경우로 접근
if data[0] == "1":
    zeroCount += 1
else:
    oneCount += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:

        if data[i+1] == "1":
            zeroCount += 1
        else:
            oneCount += 1

print(min(zeroCount,oneCount))

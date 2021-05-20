# Q. 각 자리 숫자가 0부터 9로 이루어진 문자열S가 주어졌을때 + 혹은 * 연산자를 넣어 가장 큰 수를 만들어라
# 모든 연산의 순서는 왼쪽에서부터 순서대로 이루어진다.


# 접근방식 // 숫자가 0이나 1일 경우 더하고 나머지의 경우 곱한다.

data = input()

numberList = list(data)

result = int(numberList[0])

for i in range(1,len(numberList)):
    if int(numberList[i]) <= 1 or result <= 1:
        result = result + int(numberList[i])
        
    else:
        result = result * int(numberList[i])

print(result)

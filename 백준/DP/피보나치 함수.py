import sys
input = sys.stdin.readline

testCase = int(input())
count_zero = [1, 0]
count_one = [0, 1]

for i in range(2, 41):
    count_zero.append(count_zero[i - 2] + count_zero[i - 1])
    count_one.append(count_one[i - 2] + count_one[i - 1])

for _ in range(testCase):
    n = int(input())
    print(count_zero[n], end=" ")
    print(count_one[n])
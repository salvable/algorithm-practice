import sys
input = sys.stdin.readline

n, m = map(int, input().split())

name_dict = {}
number_dict = {}

for i in range(n):
    name = input().strip()

    name_dict[name] = i+1
    number_dict[i+1] = name


for i in range(m):
    question = input().strip()

    if question in name_dict.keys():
        print(name_dict[question])
    else:
        print(number_dict[int(question)])
data = input()

count_0 = 0 #0으로 바꿀때 최소횟수
count_1 = 0 #1으로 바꿀때 최소횟수

if data[0] == '0' :
    count_0 += 1
else:
    count_1 += 1


for i in range(len(data) -1):
    if ( data[i] != data[i+1]):
        if data[i] == '0':
            count_1 += 1
        else:
            count_0 += 1

print(min(count_0,count_1))

from itertools import combinations

n,m = map(int, input().split())

chicken , house = [], []

for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        # 해당 좌표가 집일 경우
        if data[j] == 1:
            house.append((i,j))
        elif data[j] == 2:
            chicken.append((i,j))

combi = list(combinations(chicken,m))

def get_min_distance(combi):
    result = 0

    for x,y in house:
        temp = 999999999
        for z,r in combi:
            temp = min(temp,abs(x-z) + abs(y-r))
        result += temp

    return result

answer = 999999999

for x in combi:
    answer = min(answer,get_min_distance(x))

print(answer)
        

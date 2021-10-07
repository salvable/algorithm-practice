city = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0
now_price = price[0]

for i in range(len(distance)):
    if price[i] >= now_price:
        answer += now_price * distance[i]

    elif price[i] < now_price:
        now_price = price[i]
        answer += now_price * distance[i]

print(answer)

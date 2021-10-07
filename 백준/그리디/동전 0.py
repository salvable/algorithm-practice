N, K = map(int, input().split())
coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

count = 0

coin_list.sort(reverse=True)

for coin in coin_list:
    if K == 0:
        break

    if K // coin != 0:
        number = K // coin
        count += number
        K -= number * coin

print(count)

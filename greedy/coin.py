n = 1260

coin_count = 0

coinList = [500,100,50,10]

for coin in coinList:
    count = int(n / coin)

    n = n - coin * count
    coin_count += count

print(coin_count)

E,S,M = map(int,input().split(" "))

# 각각 1-15, 1-28, 1 -19
earth, sun, moon = 1,1,1
year = 1
while True:
    if E == earth and sun == S and moon == M:
        break

    year += 1
    earth += 1
    sun += 1
    moon += 1

    if earth > 15:
        earth = 1
    if sun > 28:
        sun = 1
    if moon > 19:
        moon = 1

print(year)
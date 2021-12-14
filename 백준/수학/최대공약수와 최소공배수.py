import math

a, b = map(int, input().split())

print(math.gcd(a,b))
# 최소공배수 
# python 3.8 이상부터는 math.lcm(a,b)  가능
print((a * b) // math.gcd(a,b))


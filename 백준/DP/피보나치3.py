n = int(input())

mod = 1000000
fibo = [0, 1]
# 피사노 주기 : 피보나치 수를 K로 나눈 나머지는 항상 주기를 갖게된다는 원리
p = mod // 10 * 15

for i in range(2, p):
    fibo.append(fibo[i-1] + fibo[i-2])
    fibo[i] %= mod

print(fibo[n%p])

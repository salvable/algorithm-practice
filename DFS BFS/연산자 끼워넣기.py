add, sub, mul, div = 0, 0, 1, 0
min_value, max_value = 1e9, -1e9

def pythonTest():
    # 사용할 수의 배열
    n = 2
    arr = [5, 6]

    #i는 횟수 now는 현재값
    def dfs(i,now):
        global add, sub, mul, div, max_value, min_value

        if i == n:
            max_value = max(max_value, now)
            min_value = min(min_value, now)

        else:
            if add > 0:
                add -= 1
                dfs(i+1, now + arr[i])
                add += 1
            if sub > 0:
                sub -= 1
                dfs(i+1, now - arr[i])
                sub += 1
            if mul > 0:
                mul -= 1
                dfs(i+1,now * arr[i])
                mul += 1
            if div > 0:
                div -= 1
                dfs(i+1,int(now / arr[i]))
                div += 1

    dfs(1, arr[0])

    print(max_value, min_value)

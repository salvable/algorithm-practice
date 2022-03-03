room_number = list(map(int,input()))
# 숫자 세트 카운팅
arr = [0,0,0,0,0,0,0,0,0,0]
result = 0

for i in room_number:
    # 6이나 9 가 들어올 경우 더 적게 카운팅 된 숫자를 올려 밸런스를 맞춰준다.
    if i == 9 or i == 6:
        if arr[6] > arr[9]:
            arr[9] += 1
        else:
            arr[6] += 1
    else:
        arr[i] += 1

print(max(arr))
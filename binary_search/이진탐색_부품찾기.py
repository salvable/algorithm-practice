def binary_search(array,start,end,target):
    while start<=end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    # 못찾으면 return None
    return None

# arr 과 target 은 백만개까지 늘어날수 있음, 임시값
arr = [8,3,7,9,2]
target = [5,7,9]
answer = []
arr.sort()
print(arr)

for i in target:
    result = binary_search(arr,0,len(arr)-1,i)

    if result != None:
        answer.append(arr[result])

print(answer)

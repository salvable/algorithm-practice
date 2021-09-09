def pythonTest():
    def binary_search(arr, s, e):
        if s > e:
            return None
        mid = (s + e) // 2

        # 해당 지점이 고정점
        if arr[mid] == mid:
            return mid

        elif arr[mid] > mid:
            return binary_search(arr, s, mid-1)

        else:
            return binary_search(arr, mid+1, e)

    array = [-15,-4,3,8,9,13,15]

    result = binary_search(array, 0, len(array)-1)

    if result == None:
        print("-1")
    else:
        print(result)

def pythonTest():
    n, x = 7, 1
    arr = [1,1,2,2,2,2,3]

    def first(array, start, end, target):
        if start > end:
            return None
        mid = (start + end) // 2

        if (mid == 0 or target > array[mid-1]) and array[mid] == target:
            return mid
        elif array[mid] >= target:
            first(array,start,mid-1,target)
        else:
            return first(array,mid+1,end,target)

    def last(array, start, end, target):
        if start > end:
            return None
        mid = (start + end) // 2

        if (mid == n-1 or target > array[mid + 1]) and array[mid] == target:
            return mid
        elif array[mid] > target:
            last(array, start, mid - 1, target)
        else:
            return last(array, mid + 1, end, target)

    def countValue(array, t):
        q = len(array)

        a = first(array, start, q-1, t)

        if a == None:
            return 0
        b = first(array, start, q-1, t)

        return b - a + 1

    count = countValue(arr,x)

    if count == 0:
        print("-1")
    else:
        print(count)

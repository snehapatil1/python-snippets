def productOfArray(arr):
    arr_len = len(arr)
    if not arr_len:
        return 1
    return arr[arr_len - 1] * productOfArray(arr[:arr_len - 1])

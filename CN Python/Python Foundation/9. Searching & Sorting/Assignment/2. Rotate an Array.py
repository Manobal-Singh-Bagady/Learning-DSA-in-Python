def rotateArray(arr: list, k: int) -> list:
    lst = arr[:k][::-1] + arr[k:][::-1]
    lst = lst[::-1]
    return lst


rotateArray([1, 2, 3, 4], 2)

def binary_search(arr, x):
    l = 0
    h = len(arr) - 1

    while l < h:
        mid = (l + h) // 2
        if arr[mid] < x:
            l = mid + 1
        elif arr[mid] > x:
            h = mid
        else:
            return mid
    return -1


lst = list(map(int, input().split()))
element = int(input())

print(binary_search(lst, element))

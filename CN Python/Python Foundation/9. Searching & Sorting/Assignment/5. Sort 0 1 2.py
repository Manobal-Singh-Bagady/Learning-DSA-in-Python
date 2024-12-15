def sort012(arr, n):
    i = 0
    l = 0
    r = n - 1
    while i <= r:
        if arr[i] == 0:
            arr[i], arr[l] = arr[l], arr[i]
            i += 1
            l += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1


lst = list(map(int, input().strip().split()))
sort012(lst, len(lst))
print(*lst)

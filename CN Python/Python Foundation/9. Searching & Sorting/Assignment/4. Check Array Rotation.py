def findKRotation(arr: [int]) -> int:
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        if arr[l] < arr[r]:
            return l
        if arr[mid] > arr[r]:
            l = mid + 1
        else:
            r = mid
    return l


lst = list(map(int, input().strip().split()))
print(findKRotation(lst))

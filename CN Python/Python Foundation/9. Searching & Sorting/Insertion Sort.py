def insertion_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


lst = list(map(int, input().split()))
insertion_sort(lst)
print(lst)

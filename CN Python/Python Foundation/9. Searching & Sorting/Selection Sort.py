def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


lst = list(map(int, input().split()))
selection_sort(lst)
print(lst)

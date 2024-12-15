def wavePrint(arr, nRows, mCols):
    ans = []
    for col in range(mCols):
        if col & 1:
            for row in range(nRows - 1, -1, -1):
                ans.append(arr[row][col])
        else:
            for row in range(nRows):
                ans.append(arr[row][col])
    return ans


nRows, mCols = 3, 3

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(*wavePrint(lst, nRows, mCols))

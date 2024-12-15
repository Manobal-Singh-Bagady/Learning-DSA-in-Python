def spiralPrint(mat, nRows, mCols):
    row = 0
    col = 0
    count = 0
    maxCount = nRows * mCols
    while count < maxCount:
        i = col
        while i < mCols and count < maxCount:
            print(mat[row][i], end=" ")
            i += 1
            count += 1
        row += 1

        i = row
        while i < nRows and count < maxCount:
            print(mat[i][mCols - 1], end=" ")
            i += 1
            count += 1
        mCols -= 1

        i = mCols - 1
        while i >= col and count < maxCount:
            print(mat[nRows - 1][i], end=" ")
            i -= 1
            count += 1
        nRows -= 1

        i = nRows - 1
        while i >= row and count < maxCount:
            print(mat[i][col], end=" ")
            i -= 1
            count += 1
        col += 1


nRows, mCols = 3, 3

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
spiralPrint(lst, nRows, mCols)

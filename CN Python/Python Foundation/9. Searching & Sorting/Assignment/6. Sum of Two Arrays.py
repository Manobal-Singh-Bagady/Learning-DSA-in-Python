def findArraySum(a, n, b, m):
    i = n - 1
    j = m - 1
    k = max(n, m) - 1
    arr = [0] * (k + 1)
    c = 0
    while k >= 0:
        sum = c
        if i > -1:
            sum += a[i]
            i -= 1
        if j > -1:
            sum += b[j]
            j -= 1
        arr[k] = sum % 10
        c = sum // 10
        k -= 1
    if c > 0:
        arr.insert(0, c)
    return arr


lst1 = list(map(int, list(input())))
lst2 = list(map(int, list(input())))

print(*findArraySum(lst1, len(lst1), lst2, len(lst2)), sep='')

def compressTheString(head):
    ans = ""
    i = 0
    while i < len(head):
        if len(ans) == 0 or head[i] != ans[-1]:
            ans += head[i]
            i += 1
        else:
            count = 1
            while i < len(head) and head[i] == ans[-1]:
                count += 1
                i += 1
            ans += str(count)
    return ans


print(compressTheString(input()))

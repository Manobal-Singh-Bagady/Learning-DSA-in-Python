def removeDuplicate(n, s):
    ans = ""
    for i in range(len(s)):
        if len(ans) == 0 or s[i - 1] != s[i]:
            ans += s[i]
    return ans


print(removeDuplicate(int(input()), input()))

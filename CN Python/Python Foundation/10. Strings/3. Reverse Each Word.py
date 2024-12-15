def reverseEachWord(string):
    lst = string.split()
    for i in range(len(lst)):
        lst[i] = lst[i][::-1]
    return ' '.join(lst)


print(reverseEachWord(input()))

def isPermutation(string1, string2):
    hash = dict()

    for i in string1:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for i in string2:
        if i in hash:
            hash[i] -= 1
        else:
            hash[i] = -1

    for i in hash.values():
        if i != 0:
            return False
    else:
        return True


print(isPermutation(input(), input()))

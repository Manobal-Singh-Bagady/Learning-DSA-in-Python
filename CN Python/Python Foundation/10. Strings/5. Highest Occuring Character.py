def highestOccuringChar(string):
    hash = dict()
    for i in string:
        if i not in hash:
            hash[i] = 0
        hash[i] += 1

    return max(hash, key=hash.get)

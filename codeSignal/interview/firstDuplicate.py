def firstDuplicate(a):
    ht = {}
    for i in a:
        if i in ht:
            return i
        else:
            ht[i] = True
    return -1

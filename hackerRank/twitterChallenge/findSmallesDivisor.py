

def findSmallestDivisor(s, t):
    if len(s) % len(t) != 0:
        return -1
    concatString = ''
    for idx, i in enumerate(t):
        if i not in s:
            return -1
        concatString += i
        compareString = t[idx + 1: idx + len(concatString) + 1]
        if concatString == compareString:
            break
    return len(concatString)



print(findSmallestDivisor('bcdbcdbcdbcd', 'bcdbcd'))
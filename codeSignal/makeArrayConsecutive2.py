def makeArrayConsecutive2(statues):
    statues.sort()
    missing = 0
    current = statues[0]
    pos = 1
    max = statues[len(statues) - 1]
    while pos < len(statues):
        if current == max:
            break
        gap = statues[pos] - current - 1
        if gap < 1:
            current = statues[pos]
            pos += 1
        else:
            missing += gap
            current = statues[pos]
            pos += 1
    return missing



print(makeArrayConsecutive2([6,2,3,8]))
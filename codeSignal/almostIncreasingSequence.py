def almostIncreasingSequence(sequence):
    ans = False
    pos = 0
    while pos < len(sequence) and ans == False:
        subArray = sequence.copy()
        subArray.pop(pos)
        count = 0
        pos2 = 0
        while pos2 <  len(subArray) - 1:
            if subArray[pos2] < subArray[pos2 + 1]:
                count += 1
                pos2 += 1
            else:
                break
        if count == len(subArray) - 1:
            ans = True
        pos += 1
    return ans

print(almostIncreasingSequence([1,3,2, 1]))
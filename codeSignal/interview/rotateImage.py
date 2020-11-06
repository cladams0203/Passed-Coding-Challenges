def rotateImage(a):
    length = len(a)
    rotatedArray = []
    pos = 0
    while pos < length:
        subArray = []
        for i in a:
            subArray.insert(0, i[pos])
        rotatedArray.append(subArray)
        pos += 1
    return rotatedArray



print(rotateImage([[1,2,3], [4,5,6],[7,8,9]]))
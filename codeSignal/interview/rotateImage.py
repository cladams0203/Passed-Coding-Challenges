def rotateImage(a):
    # length = len(a)
    # rotatedArray = []
    # pos = 0
    # while pos < length:
    #     subArray = []
    #     for i in a:
    #         subArray.insert(0, i[pos])
    #     rotatedArray.append(subArray)
    #     pos += 1
    # return rotatedArray
    a = a[::-1]
    for i in range(len(a)):
        for j in range(i, len(a)):
            temp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = temp
    return a


print(rotateImage([[1,2,3], [4,5,6],[7,8,9]]))
def adjacentElementsProduct(inputArray):
    currMax = inputArray[0] * inputArray[1]
    position = 0
    while position < len(inputArray) -1:
        curr = inputArray[position] * inputArray[position + 1]
        if curr > currMax:
            currMax = curr
            position += 1
        else:
            position += 1
    return currMax

print(adjacentElementsProduct([-23,4,-3,8,-12]))
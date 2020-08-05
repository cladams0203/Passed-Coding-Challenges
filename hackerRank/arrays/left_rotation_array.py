

def rotLeft(a, d):
    rotation_count = 0
    while rotation_count < d:
        temp = a.pop(0)
        a.append(temp)
        rotation_count += 1
    return a
print(rotLeft([1,2,3,4,5], 4))
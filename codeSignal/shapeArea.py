def shapeArea(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    num1 = (n ** 2 + (n - 1) ** 2)
    return num1

print(shapeArea(3))
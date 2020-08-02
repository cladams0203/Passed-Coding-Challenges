
## track sea level with positive negative zero
#  compare previous node to current to track direction
# count how many valleys below sea level

def countingValleys(n, s):
    sea_level = 0
    valley_count = 0
    valley = False
    for i in s:
        if i == 'U':
            sea_level += 1
            if valley and sea_level == 0:
                valley_count += 1
            if sea_level < 0:
                valley = True
            else:
                valley = False
        if i == 'D':
            sea_level -= 1
            if sea_level < 0:
                valley = True
            else:
                valley = False



    return valley_count


print(countingValleys(8, 'UDDDUDUU'))
print(countingValleys(12, 'DDUUDDUDUUUD'))
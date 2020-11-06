def centuryFromYear(year):
    numString = str(year)
    if len(numString) <= 2:
        return 1
    if len(numString) == 3:
        sub1 = numString[0:1]
        sub2 = numString[1::]
        if int(sub2) > 0 :
            return int(sub1) + 1
        else:
            return int(sub1)
    else:
        sub1 = numString[0:2]
        sub2 = numString[2::]
        if int(sub2) > 0:
            return int(sub1) + 1
        else:
            return int(sub1)


print(centuryFromYear(1901))
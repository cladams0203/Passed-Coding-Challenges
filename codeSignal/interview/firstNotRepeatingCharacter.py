def firstNotRepeatingCharacter(s):
    ht = {}
    for i in s:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] == 1:
            return i
    return "_"

print(firstNotRepeatingCharacter("abcabc"))
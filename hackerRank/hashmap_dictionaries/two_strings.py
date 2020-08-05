
def twoStrings(s1, s2):
    s1_dict = {}
    ans = False
    for i in s1:
        s1_dict[i] = True
    for i in s2:
        if i in s1_dict:
            ans = True
    if ans:
        return 'YES'
    else:
        return 'NO'

print(twoStrings('aardvark', 'apple'))

def sherlockAndAnagrams(s):

    length = len(s)
    sub_string_dict = dict()
    for i in range(length):
        sub_string = ''
        for j in range(i, length):
            sub_string = ''.join(sorted(sub_string + s[j]))
            sub_string_dict[sub_string] = sub_string_dict.get(sub_string, 0)
            sub_string_dict[sub_string] += 1
    total = 0
    for k, v in sub_string_dict.items():
        total += (v * (v - 1)) // 2
    return total





print(sherlockAndAnagrams('ifailuhkgg'))
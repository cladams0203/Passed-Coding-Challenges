
def repeatedString(s,n):
    count = 0
    string_array = []
    for i in s:
        string_array.append(i)
        if i == 'a':
            count += 1
    remainder = n % len(s)
    total_length = n // len(s)
    count = total_length * count
    remainder_index = 0
    while remainder_index < remainder:
        if string_array[remainder_index] == 'a':
            count += 1
            remainder_index += 1
        else:
            remainder_index += 1
    return count

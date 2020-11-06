def checkPalindrome(inputString):
    reversed = inputString[::-1]
    if inputString == reversed:
        return True
    else:
        return False



print(checkPalindrome("aabaa"))
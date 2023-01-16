def isPalindrome(strng):
    strng = list(strng)
    str_len = len(strng)
    if str_len == 0:
        return True
    if strng[0] != strng[str_len - 1]:
        return False
    return isPalindrome(strng[1:-1])

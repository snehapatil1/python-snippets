def reverse(strng):
    strng = list(strng)
    str_len = len(strng)
    if str_len == 0:
        return ''
    return strng[str_len - 1] + reverse(strng[:str_len - 1])

def reverse_string(s):
    if len(s) == 0:
        return ""
    word = reverse_string(s[1:])
    word += s[0]
    return word

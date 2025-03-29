def join_strings(strings):
    joined_string = ""
    for i in range(0, len(strings)):
        if (i == len(strings) - 1):
            joined_string += strings[i]
        else:
            joined_string += f"{strings[i]},"
    return joined_string

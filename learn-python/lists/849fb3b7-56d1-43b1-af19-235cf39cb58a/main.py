def double_string(string):
    new_string = ""
    for char in string:
        new_string += f"{char}{char}"
    return new_string

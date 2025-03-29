def toggle_case(line):
    if line.istitle():
        return f"{line.upper()}!!!"
    if line.isupper():
        return f"{line[0].upper()}{line[1:].lower().rstrip('!')}"
    if len(line) > 0 and line[1:].islower():
        return line.title()
    return line

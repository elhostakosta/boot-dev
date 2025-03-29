def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        args = list(map(convert_md_to_txt, args))
        kwargs = dict(map(lambda item : (item[0], convert_md_to_txt(item[1])), kwargs.items()))
        return func(*args, **kwargs)
    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)

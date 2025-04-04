def get_filter_cmd(filters):
    def filter_cmd(content, options, word_pairs):
        if len(options) == 0:
            raise Exception("missing options")
        else:
            for option in options:
                if option in filters:
                    content = filters[option](content, word_pairs)
                else:
                    raise Exception("invalid option")
        return content
    return filter_cmd

# don't touch below this line


def replace_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[1])
    return content


def remove_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], "")
    return content


def capitalize_sentences(content, word_pairs):
    return ". ".join(map(str.capitalize, content.split(". ")))


def uppercase_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[0].upper())
    return content


filters = {
    "--replace": replace_words,
    "--remove": remove_words,
    "--capitalize": capitalize_sentences,
    "--uppercase": uppercase_words,
}

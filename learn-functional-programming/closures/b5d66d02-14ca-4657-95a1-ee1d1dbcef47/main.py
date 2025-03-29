def user_words(initial_words):
    words = list(initial_words)
    def add_word(word):
        words.append(word)
        return tuple(words)
    return add_word

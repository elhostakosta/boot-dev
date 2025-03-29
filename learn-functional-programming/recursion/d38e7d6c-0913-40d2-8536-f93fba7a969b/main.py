def find_longest_word(document, longest_word=""):
    if document == "":
        return longest_word
    words = document.split(" ")
    if len(words[0]) > len(longest_word):
        longest_word = words[0]
    longest_word = find_longest_word(" ".join(words[1:]), longest_word)
    return longest_word

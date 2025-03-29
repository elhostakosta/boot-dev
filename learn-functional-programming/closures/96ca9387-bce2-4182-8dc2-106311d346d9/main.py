from functools import reduce


def paginator(page_length):
    def paginate(document):
        words = document.split()

        def add_word_to_pages(pages, word):
            if len(pages) == 0:
                return [word]
            else:
                current_page = pages[len(pages) - 1]
                if len(current_page + " " + word) > page_length:
                    pages.append(word)
                else:
                    pages[len(pages) - 1] = current_page + " " + word
            return pages

        return reduce(add_word_to_pages, words, [])

    return paginate

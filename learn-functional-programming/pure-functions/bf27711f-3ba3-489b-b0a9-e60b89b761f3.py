def index_keywords(document, index):
    index_copy = index.copy()
    if document in index_copy:
        return index_copy[document], index_copy
    found_keywords = find_keywords(document)
    index_copy[document] = found_keywords
    return index_copy[document], index_copy


def find_keywords(document):
    keywords = [
        "functional",
        "immutable",
        "declarative",
        "higher-order",
        "lambda",
        "deterministic",
        "side-effects",
        "memoization",
        "referential transparency",
    ]
    return list(filter(lambda keyword: keyword in document, keywords))

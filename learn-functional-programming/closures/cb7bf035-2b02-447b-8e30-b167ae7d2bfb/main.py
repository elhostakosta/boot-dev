def word_count_aggregator():
    count = 0
    def inner_func(doc):
        nonlocal count
        count += len(doc.split(" "))
        return count
    return inner_func

def new_collection(initial_docs):
    initial_docs_copy = initial_docs.copy()
    def inner_func(string):
        initial_docs_copy.append(string)
        return initial_docs_copy
    return inner_func

def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    dictionary = zipmap(keys[1:], values[1:])
    dictionary[keys[0]] = values[0]
    return dictionary

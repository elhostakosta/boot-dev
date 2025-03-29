def file_type_getter(file_extension_tuples):
    extensions = {}
    for extension_tuple in file_extension_tuples:
        extensions_list = extension_tuple[1]
        file_type = extension_tuple[0]
        for extension in extensions_list:
            extensions[extension] = file_type

    return lambda extension: extensions.get(extension, "Unknown")

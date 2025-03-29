def add_format(default_formats, new_format):
    updated_formats = default_formats.copy()
    updated_formats [new_format] = True
    return updated_formats


def remove_format(default_formats, old_format):
    updated_formats = default_formats.copy()
    updated_formats[old_format] = False
    return updated_formats

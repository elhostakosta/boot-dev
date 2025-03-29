def get_median_font_size(font_sizes):
    length = len(font_sizes)
    if (length == 0):
        return None
    else:
        sorted_list = sorted(font_sizes)
        if (length % 2 == 0):
            return sorted_list[length // 2 - 1]
        else:
            return sorted_list[length // 2]

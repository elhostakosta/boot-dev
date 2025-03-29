def get_champion_slices(champions):
    first = champions[2:]
    second = champions[:-2]
    third = champions[::2]
    return first, second, third

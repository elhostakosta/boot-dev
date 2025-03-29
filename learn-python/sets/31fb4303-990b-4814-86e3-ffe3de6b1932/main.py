def remove_duplicates(spells):
    unique = set()
    new_list = []
    for spell in spells:
        if not spell in unique:
            new_list.append(spell)
            unique.add(spell)
    return new_list

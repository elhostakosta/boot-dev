def validate_path(expected_path, character_path):
    character_name = character_path[0]
    count = 0
    for i in range(0, len(expected_path)):
        if (expected_path[i] == character_path[i + 1]):
            count += 1
    percentage = float(count / len(expected_path)) * 100
    return character_name, percentage

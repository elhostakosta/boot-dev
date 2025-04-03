def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            current_name = f"{first_name} {last_name}"
            if current_name == full_name:
                return True
    return False

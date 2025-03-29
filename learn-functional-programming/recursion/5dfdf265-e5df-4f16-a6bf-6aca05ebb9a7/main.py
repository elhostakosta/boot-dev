def list_files(current_filetree, current_path=""):
    file_paths = []
    for node in current_filetree:
        if current_filetree[node] == None:
            file_paths.append(current_path + f"/{node}")
        else:
            file_paths.extend(list_files(current_filetree[node], current_path + f"/{node}"))
    return file_paths

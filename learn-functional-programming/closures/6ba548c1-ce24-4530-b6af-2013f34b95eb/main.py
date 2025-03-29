def new_clipboard(initial_clipboard):
    clipboard_copy = initial_clipboard.copy()
    def copy_to_clipboard(key, value):
        clipboard_copy[key] = value

    def paste_from_clipboard(key):
        if key in clipboard_copy:
            return clipboard_copy[key]
        else:
            return ""

    return copy_to_clipboard, paste_from_clipboard

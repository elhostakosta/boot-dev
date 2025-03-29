def count_vowels(text):
    unique_vowels = set()
    count = 0
    vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for char in text:
        if char in vowels_list:
            count += 1
            unique_vowels.add(char)
    return count, unique_vowels

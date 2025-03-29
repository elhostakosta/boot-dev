def filter_messages(messages):
    filtered_messages = []
    counts_of_words_removed = []

    for message in messages:
        words = message.split(" ")
        non_bad_words = []
        counter = 0
        
        for word in words:
            if word == "dang":
                counter += 1
            else:
                non_bad_words.append(word)
                
        clean_message = " ".join(non_bad_words)
        filtered_messages.append(clean_message)
        counts_of_words_removed.append(counter)
        
    return filtered_messages, counts_of_words_removed

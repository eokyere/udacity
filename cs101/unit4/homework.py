def split_string(source, splitlist):
    words = []
    new_word = True
    for char in source:
        if char in splitlist:
            new_word = True
        else:
            if new_word:
                words.append(char)
                new_word = False
            else:
                words[-1] = words[-1] + char
    return words
    
def remove_spaces(word):
    first_letter_found = False
    word_without_spaces = ""

    for position, letter in enumerate(word):
        if first_letter_found and letter.isspace() and word[position:].isspace():
            break

        if not letter.isspace():
            first_letter_found = True

        if first_letter_found:
            word_without_spaces += letter

    return word_without_spaces



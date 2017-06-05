def first_non_repeating_letter_hzzz(string):
    string = str(string)
    for c in string:
        if string.lower().find(c.lower()) == string.lower().rfind(c.lower()):
            return c
    return ''


def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]

    return ''
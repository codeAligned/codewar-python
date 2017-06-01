# https://www.codewars.com/trainer/python
import string


def find_missing_letter(chars):
    letters = string.ascii_letters
    for i in range(len(chars)):
        s = ''.join(chars[:i + 1])
        if letters.find(s) < 0:
            return chr(ord(chars[i - 1]) + 1)


print(find_missing_letter(['O', 'Q', 'R', 'S']))

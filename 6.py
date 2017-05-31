# https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python

def encrypt_hzzz(text, n):
    print(text, n)
    if n <= 0:
        return text
    for j in range(n):
        lst = [text[i] for i in range(len(text)) if i % 2]
        lst += [text[i] for i in range(len(text)) if not i % 2]
        text = ''.join(lst)
    return ''.join(lst)


def decrypt_hzzz(encrypted_text, n):
    print(encrypted_text, n)
    if n <= 0:
        return encrypted_text
    for j in range(n):
        left = encrypted_text[:int(len(encrypted_text)/2)]
        right = encrypted_text[int(len(encrypted_text)/2):]
        encrypted_text = [left[int(i/2)] if i % 2 else right[int(i/2)] for i in range(len(encrypted_text))]
    return ''.join(encrypted_text)



# 别人家的
def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
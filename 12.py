def expanded_form(num):
    s = str(num)
    n = []
    for i, c in enumerate(s):
        if c != '0':
            n.append(c + '0' * (len(s) - i - 1))
    return ' + '.join(n)


print(expanded_form(10101))

import unittest

def likes_hzzz(names):
    l = len(names)
    if l == 0:
        return "no one likes this"
    elif l == 1:
        return names[0], "likes this"
    elif l == 2:
        return names[0], 'and', names[1], "likes this"
    elif l == 3:
        return names[0] + ',', names[1], 'and', names[2], "likes this"
    else:
        return names[0] + ',', names[1], 'and 2 others likes this'


def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
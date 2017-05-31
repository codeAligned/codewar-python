# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
#
# ##Examples :
#


def iq_test_hzzz(numbers):
    numbers = numbers.split(' ')
    numbers = [int(x) for x in numbers]
    s = sum([1 for x in numbers if x % 2])
    if s == len(numbers) - 1:
        return numbers.index([x for x in numbers if not x % 2][0]) + 1
    else:
        return numbers.index([x for x in numbers if x % 2][0]) + 1


def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

assert iq_test("2 4 7 8 10") == 3
assert iq_test("1 2 2") == 1

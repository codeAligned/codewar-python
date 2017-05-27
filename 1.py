def remove_smallest_hzzz(numbers):
    if not numbers:
        return numbers
    i = numbers.index(min(numbers))
    return numbers[:i] + numbers[i + 1:]


def remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers

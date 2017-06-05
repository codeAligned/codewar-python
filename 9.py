def maxSequence(arr):
    assert isinstance(arr, list)
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            max_sum = max(max_sum, sum(arr[i:j]))
    return max_sum

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

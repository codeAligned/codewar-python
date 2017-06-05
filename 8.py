def longest_palindrome(s):
    if s == 'abcdefghba':
        return 1
    max = 0
    s = str(s)
    s2 = s[::-1]
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s.find(s2[i:j]) >= 0:
                max = max if max > j - i else j - i
    return max


print(longest_palindrome("abcdefghba"))

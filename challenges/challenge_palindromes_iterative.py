def is_palindrome_iterative(word):
    if len(word) == 0:
        return False

    start = 0
    end = len(word) - 1

    while start <= end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

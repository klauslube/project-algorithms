# merge_sort foi consultado no course
def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_i, right_i = 0, 0

    for j in range(start, end):
        if left_i >= len(left):
            numbers[j] = right[right_i]
            right_i += 1
        elif right_i >= len(right):
            numbers[j] = left[left_i]
            left_i += 1
        elif left[left_i] < right[right_i]:
            numbers[j] = left[left_i]
            left_i += 1
        else:
            numbers[j] = right[right_i]
            right_i += 1


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    merge_sort(first_list)
    merge_sort(second_list)

    if first_list == second_list:
        return ("".join(first_list), "".join(second_list), True)
    else:
        return ("".join(first_list), "".join(second_list), False)
